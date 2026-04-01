#!/usr/bin/env python3
"""
NYC Construction Timelines: Filing to Completion
Analyzes how long it takes to build in NYC, using DOB permit data.

Two analytical populations:
  1. Legacy BIS system: NB jobs filed ~2004-2019, signed off by DOB
  2. DOB NOW system: NB jobs filed 2021-present (future extension)

Data sources:
  - DOB Job Application Filings (ic3t-wcy2) — legacy BIS, frozen ~2020
  - DOB Certificate of Occupancy (bs8b-p36w) — active, 2012-present
"""

import json
import urllib.request
import urllib.parse
from datetime import datetime, timedelta
from collections import defaultdict
import csv
import os

DATA_DIR = os.path.dirname(os.path.abspath(__file__))

# ── Socrata helpers ──────────────────────────────────────────────

def socrata_fetch(dataset_id, params, limit=50000):
    """Fetch records from NYC Open Data via Socrata API."""
    base = f"https://data.cityofnewyork.us/resource/{dataset_id}.json"
    params['$limit'] = str(limit)
    url = base + '?' + urllib.parse.urlencode(params)
    print(f"  Fetching {dataset_id} ({limit} limit)...")
    req = urllib.request.Request(url, headers={'Accept': 'application/json'})
    with urllib.request.urlopen(req, timeout=120) as resp:
        data = json.loads(resp.read().decode())
    print(f"  Got {len(data)} records")
    return data

def socrata_fetch_all(dataset_id, params, batch_size=50000):
    """Paginate through all matching records."""
    all_records = []
    offset = 0
    while True:
        p = dict(params)
        p['$limit'] = str(batch_size)
        p['$offset'] = str(offset)
        batch = socrata_fetch(dataset_id, p, batch_size)
        all_records.extend(batch)
        if len(batch) < batch_size:
            break
        offset += batch_size
    return all_records

# ── Date parsing ─────────────────────────────────────────────────

def parse_date_mdy(s):
    """Parse MM/DD/YYYY text date (BIS format)."""
    if not s:
        return None
    try:
        return datetime.strptime(s.strip(), '%m/%d/%Y')
    except ValueError:
        return None

def parse_date_iso(s):
    """Parse ISO datetime (Socrata calendar_date format)."""
    if not s:
        return None
    try:
        return datetime.fromisoformat(s.replace('T00:00:00.000', ''))
    except ValueError:
        return None

# ── Step 1: Pull BIS NB filings ─────────────────────────────────

def pull_bis_filings():
    """Pull all NB jobs from legacy BIS that reached sign-off."""
    cache_path = os.path.join(DATA_DIR, 'bis_nb_signedoff.json')
    if os.path.exists(cache_path):
        print("Loading cached BIS filings...")
        with open(cache_path) as f:
            return json.load(f)

    print("Pulling BIS NB signed-off jobs...")
    records = socrata_fetch_all('ic3t-wcy2', {
        '$select': 'job__,pre__filing_date,paid,fully_paid,signoff_date,borough,building_type,proposed_no_of_stories,initial_cost,pc_filed',
        '$where': "job_type='NB' AND job_status='X' AND signoff_date IS NOT NULL AND pre__filing_date IS NOT NULL",
        '$order': 'job__ ASC',
    })

    # Deduplicate by job number (BIS has some dupes)
    seen = set()
    unique = []
    for r in records:
        jn = r.get('job__')
        if jn and jn not in seen:
            seen.add(jn)
            unique.append(r)
    print(f"  Deduplicated: {len(records)} -> {len(unique)}")

    with open(cache_path, 'w') as f:
        json.dump(unique, f)
    return unique

# ── Step 2: Pull COs for NB jobs ────────────────────────────────

def pull_cos():
    """Pull all NB certificates of occupancy."""
    cache_path = os.path.join(DATA_DIR, 'co_nb.json')
    if os.path.exists(cache_path):
        print("Loading cached COs...")
        with open(cache_path) as f:
            return json.load(f)

    print("Pulling NB certificates of occupancy...")
    records = socrata_fetch_all('bs8b-p36w', {
        '$select': 'job_number,c_o_issue_date,issue_type,borough',
        '$where': "job_type='NB' AND c_o_issue_date IS NOT NULL",
        '$order': 'job_number ASC',
    })

    with open(cache_path, 'w') as f:
        json.dump(records, f)
    return records

# ── Step 2b: Pull DOB NOW NB filings ────────────────────────────

def pull_dobnow_filings():
    """Pull NB jobs from DOB NOW that have signoff dates."""
    cache_path = os.path.join(DATA_DIR, 'dobnow_nb_signedoff.json')
    if os.path.exists(cache_path):
        print("Loading cached DOB NOW filings...")
        with open(cache_path) as f:
            return json.load(f)

    print("Pulling DOB NOW NB jobs with signoff...")
    records = socrata_fetch_all('w9ak-ipjd', {
        '$select': 'job_filing_number,filing_date,first_permit_date,signoff_date,filing_status,borough,building_type,total_construction_floor_area,initial_cost',
        '$where': "job_type='New Building' AND signoff_date IS NOT NULL AND filing_date IS NOT NULL",
        '$order': 'job_filing_number ASC',
    })

    # Deduplicate by job filing number
    seen = set()
    unique = []
    for r in records:
        jn = r.get('job_filing_number')
        if jn and jn not in seen:
            seen.add(jn)
            unique.append(r)
    print(f"  Deduplicated: {len(records)} -> {len(unique)}")

    with open(cache_path, 'w') as f:
        json.dump(unique, f)
    return unique

def compute_dobnow_timelines(filings):
    """Compute durations from DOB NOW filing records."""
    results = []
    for f in filings:
        jn = f.get('job_filing_number')
        filing_dt = parse_date_iso(f.get('filing_date'))
        signoff_dt = parse_date_iso(f.get('signoff_date'))
        permit_dt = parse_date_iso(f.get('first_permit_date'))

        if not filing_dt or not signoff_dt:
            continue

        filing_year = filing_dt.year
        if filing_year < 2017 or filing_year > 2025:
            continue

        filing_to_signoff = (signoff_dt - filing_dt).days
        filing_to_permit = (permit_dt - filing_dt).days if permit_dt else None

        if filing_to_signoff < 0 or filing_to_signoff > 365 * 15:
            continue

        # DOB NOW doesn't have proposed_no_of_stories; use floor area as proxy
        sqft = 0
        try:
            sqft = float(f.get('total_construction_floor_area', 0))
        except (ValueError, TypeError):
            pass

        # Rough size proxy from floor area
        if sqft <= 5000:
            size = 'Small (1-3 fl)'
        elif sqft <= 30000:
            size = 'Mid (4-10 fl)'
        elif sqft <= 150000:
            size = 'Large (11-30 fl)'
        else:
            size = 'Tower (30+ fl)'

        # Normalize building_type to match BIS
        bt = f.get('building_type', 'Unknown')
        if bt in ('1 Family', '2 Family', '3 Family'):
            bt_norm = '1-2-3 FAMILY'
        else:
            bt_norm = 'OTHERS'

        results.append({
            'job': jn,
            'system': 'DOB NOW',
            'filing_year': filing_year,
            'borough': f.get('borough', 'Unknown').upper(),
            'building_type': bt_norm,
            'stories': 0,
            'size': size,
            'filing_to_signoff_days': filing_to_signoff,
            'filing_to_signoff_months': round(filing_to_signoff / 30.44, 1),
            'filing_to_permit_days': filing_to_permit,
            'filing_to_permit_months': round(filing_to_permit / 30.44, 1) if filing_to_permit else None,
            'filing_to_co_days': None,
            'filing_to_co_months': None,
            'has_co': False,
            'pc_filed': '',
        })

    return results

# ── Step 3: Join and compute durations ───────────────────────────

def compute_timelines(filings, cos):
    """Join filings to COs and compute duration metrics."""

    # Build CO lookup: job_number -> earliest CO date (first TCO or final CO)
    co_lookup = {}
    for co in cos:
        jn = co.get('job_number')
        if not jn:
            continue
        dt = parse_date_iso(co.get('c_o_issue_date'))
        if not dt or dt.year > 2030:  # filter garbage dates
            continue
        if jn not in co_lookup or dt < co_lookup[jn]:
            co_lookup[jn] = dt

    print(f"CO lookup: {len(co_lookup)} unique NB job numbers with COs")

    results = []
    for f in filings:
        jn = f.get('job__')
        filing_dt = parse_date_mdy(f.get('pre__filing_date'))
        signoff_dt = parse_date_mdy(f.get('signoff_date'))

        if not filing_dt or not signoff_dt:
            continue

        filing_year = filing_dt.year
        # Focus on 2004-2019 filings (reliable BIS era)
        if filing_year < 2004 or filing_year > 2019:
            continue

        # Filing-to-signoff duration
        filing_to_signoff = (signoff_dt - filing_dt).days

        # Filing-to-CO duration (if CO exists)
        co_dt = co_lookup.get(jn)
        filing_to_co = (co_dt - filing_dt).days if co_dt else None

        # Sanity: skip negative or absurdly long durations
        if filing_to_signoff < 0 or filing_to_signoff > 365 * 20:
            continue
        if filing_to_co is not None and (filing_to_co < 0 or filing_to_co > 365 * 20):
            filing_to_co = None

        stories = 0
        try:
            stories = int(f.get('proposed_no_of_stories', 0))
        except (ValueError, TypeError):
            pass

        # Classify building size
        if stories <= 3:
            size = 'Small (1-3 fl)'
        elif stories <= 10:
            size = 'Mid (4-10 fl)'
        elif stories <= 30:
            size = 'Large (11-30 fl)'
        else:
            size = 'Tower (30+ fl)'

        results.append({
            'job': jn,
            'system': 'BIS',
            'filing_year': filing_year,
            'borough': f.get('borough', 'Unknown'),
            'building_type': f.get('building_type', 'Unknown'),
            'stories': stories,
            'size': size,
            'filing_to_signoff_days': filing_to_signoff,
            'filing_to_signoff_months': round(filing_to_signoff / 30.44, 1),
            'filing_to_co_days': filing_to_co,
            'filing_to_co_months': round(filing_to_co / 30.44, 1) if filing_to_co else None,
            'has_co': co_dt is not None,
            'pc_filed': f.get('pc_filed', ''),
        })

    return results

# ── Step 4: Analyze ──────────────────────────────────────────────

def median(values):
    if not values:
        return None
    s = sorted(values)
    n = len(s)
    if n % 2 == 0:
        return (s[n//2 - 1] + s[n//2]) / 2
    return s[n//2]

def percentile(values, p):
    if not values:
        return None
    s = sorted(values)
    k = (len(s) - 1) * p / 100
    f = int(k)
    c = f + 1 if f + 1 < len(s) else f
    return s[f] + (k - f) * (s[c] - s[f])

def analyze(results):
    """Produce summary statistics."""

    print(f"\n{'='*70}")
    print(f"NYC CONSTRUCTION TIMELINES: FILING TO COMPLETION")
    print(f"{'='*70}")
    print(f"\nTotal matched records: {len(results)}")
    print(f"Records with CO: {sum(1 for r in results if r['has_co'])}")

    # Use filing-to-signoff as primary metric (more complete than CO)
    metric = 'filing_to_signoff_months'
    metric_label = 'Filing to sign-off (months)'

    # ── By filing year ──
    print(f"\n{'─'*70}")
    print(f"MEDIAN {metric_label.upper()} BY FILING YEAR")
    print(f"{'─'*70}")
    print(f"{'Year':<8} {'Count':>8} {'Median':>10} {'25th':>10} {'75th':>10} {'90th':>10}")
    by_year = defaultdict(list)
    for r in results:
        by_year[r['filing_year']].append(r[metric])

    for year in sorted(by_year.keys()):
        vals = by_year[year]
        print(f"{year:<8} {len(vals):>8,} {median(vals):>10.1f} {percentile(vals, 25):>10.1f} {percentile(vals, 75):>10.1f} {percentile(vals, 90):>10.1f}")

    # ── By borough ──
    print(f"\n{'─'*70}")
    print(f"MEDIAN {metric_label.upper()} BY BOROUGH")
    print(f"{'─'*70}")
    print(f"{'Borough':<20} {'Count':>8} {'Median':>10} {'25th':>10} {'75th':>10}")
    by_boro = defaultdict(list)
    for r in results:
        by_boro[r['borough']].append(r[metric])

    for boro in sorted(by_boro.keys(), key=lambda b: median(by_boro[b]) or 0, reverse=True):
        vals = by_boro[boro]
        print(f"{boro:<20} {len(vals):>8,} {median(vals):>10.1f} {percentile(vals, 25):>10.1f} {percentile(vals, 75):>10.1f}")

    # ── By building size ──
    print(f"\n{'─'*70}")
    print(f"MEDIAN {metric_label.upper()} BY BUILDING SIZE")
    print(f"{'─'*70}")
    print(f"{'Size':<20} {'Count':>8} {'Median':>10} {'25th':>10} {'75th':>10}")
    by_size = defaultdict(list)
    for r in results:
        by_size[r['size']].append(r[metric])

    for size in ['Small (1-3 fl)', 'Mid (4-10 fl)', 'Large (11-30 fl)', 'Tower (30+ fl)']:
        vals = by_size.get(size, [])
        if vals:
            print(f"{size:<20} {len(vals):>8,} {median(vals):>10.1f} {percentile(vals, 25):>10.1f} {percentile(vals, 75):>10.1f}")

    # ── By building type ──
    print(f"\n{'─'*70}")
    print(f"MEDIAN {metric_label.upper()} BY BUILDING TYPE")
    print(f"{'─'*70}")
    print(f"{'Type':<20} {'Count':>8} {'Median':>10}")
    by_type = defaultdict(list)
    for r in results:
        by_type[r['building_type']].append(r[metric])

    for bt in sorted(by_type.keys(), key=lambda b: median(by_type[b]) or 0, reverse=True):
        vals = by_type[bt]
        print(f"{bt:<20} {len(vals):>8,} {median(vals):>10.1f}")

    # ── Year x Borough heatmap data ──
    print(f"\n{'─'*70}")
    print(f"MEDIAN MONTHS BY YEAR x BOROUGH (2010-2019)")
    print(f"{'─'*70}")
    boros = ['MANHATTAN', 'BROOKLYN', 'QUEENS', 'BRONX', 'STATEN ISLAND']
    print(f"{'Year':<8}", end='')
    for b in boros:
        print(f"  {b[:6]:>8}", end='')
    print()

    for year in range(2010, 2020):
        print(f"{year:<8}", end='')
        for b in boros:
            vals = [r[metric] for r in results if r['filing_year'] == year and r['borough'] == b]
            if vals:
                print(f"  {median(vals):>8.1f}", end='')
            else:
                print(f"  {'—':>8}", end='')
        print()

    # ── CO-based analysis (subset with COs) ──
    co_results = [r for r in results if r['has_co']]
    if co_results:
        print(f"\n{'─'*70}")
        print(f"FILING TO CO (MONTHS) BY YEAR — {len(co_results)} jobs with COs")
        print(f"{'─'*70}")
        print(f"{'Year':<8} {'Count':>8} {'Median':>10} {'25th':>10} {'75th':>10}")
        by_year_co = defaultdict(list)
        for r in co_results:
            by_year_co[r['filing_year']].append(r['filing_to_co_months'])

        for year in sorted(by_year_co.keys()):
            vals = by_year_co[year]
            print(f"{year:<8} {len(vals):>8,} {median(vals):>10.1f} {percentile(vals, 25):>10.1f} {percentile(vals, 75):>10.1f}")

    return results

# ── Step 5: Export ───────────────────────────────────────────────

def export_csv(results, filename='timelines.csv'):
    path = os.path.join(DATA_DIR, filename)
    fields = ['job', 'system', 'filing_year', 'borough', 'building_type', 'stories', 'size',
              'filing_to_signoff_days', 'filing_to_signoff_months',
              'filing_to_permit_days', 'filing_to_permit_months',
              'filing_to_co_days', 'filing_to_co_months', 'has_co', 'pc_filed']
    with open(path, 'w', newline='') as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        w.writerows(results)
    print(f"\nExported {len(results)} records to {path}")

# ── Step 6: Export combined JSON for charts ──────────────────────

def export_chart_data(bis_results, now_results):
    """Export pre-aggregated data for the HTML chart page."""
    all_results = bis_results + now_results

    # Tag BIS results
    for r in bis_results:
        r.setdefault('system', 'BIS')

    # ── By year (all) ──
    by_year = defaultdict(list)
    for r in all_results:
        by_year[r['filing_year']].append(r['filing_to_signoff_months'])

    year_data = []
    for year in sorted(by_year.keys()):
        vals = by_year[year]
        system = 'BIS' if year < 2017 else ('DOB NOW' if year > 2020 else 'Overlap')
        # For overlap years, split by actual system
        if 2017 <= year <= 2020:
            bis_vals = [r['filing_to_signoff_months'] for r in bis_results if r['filing_year'] == year]
            now_vals = [r['filing_to_signoff_months'] for r in now_results if r['filing_year'] == year]
            if bis_vals:
                year_data.append({'year': year, 'system': 'BIS', 'n': len(bis_vals),
                                  'median': round(median(bis_vals), 1),
                                  'p25': round(percentile(bis_vals, 25), 1),
                                  'p75': round(percentile(bis_vals, 75), 1),
                                  'p10': round(percentile(bis_vals, 10), 1),
                                  'p90': round(percentile(bis_vals, 90), 1)})
            if now_vals:
                year_data.append({'year': year, 'system': 'DOB NOW', 'n': len(now_vals),
                                  'median': round(median(now_vals), 1),
                                  'p25': round(percentile(now_vals, 25), 1),
                                  'p75': round(percentile(now_vals, 75), 1),
                                  'p10': round(percentile(now_vals, 10), 1),
                                  'p90': round(percentile(now_vals, 90), 1)})
        else:
            year_data.append({'year': year, 'system': system, 'n': len(vals),
                              'median': round(median(vals), 1),
                              'p25': round(percentile(vals, 25), 1),
                              'p75': round(percentile(vals, 75), 1),
                              'p10': round(percentile(vals, 10), 1),
                              'p90': round(percentile(vals, 90), 1)})

    # ── By borough x year ──
    boro_year_data = []
    for boro in ['MANHATTAN', 'BROOKLYN', 'QUEENS', 'BRONX', 'STATEN ISLAND']:
        for year in range(2004, 2026):
            vals = [r['filing_to_signoff_months'] for r in all_results if r['filing_year'] == year and r['borough'] == boro]
            if len(vals) >= 10:  # min sample
                boro_year_data.append({'borough': boro, 'year': year, 'n': len(vals),
                                       'median': round(median(vals), 1),
                                       'p25': round(percentile(vals, 25), 1),
                                       'p75': round(percentile(vals, 75), 1)})

    # ── By building size x year ──
    size_year_data = []
    for size in ['Small (1-3 fl)', 'Mid (4-10 fl)', 'Large (11-30 fl)', 'Tower (30+ fl)']:
        for year in range(2004, 2026):
            vals = [r['filing_to_signoff_months'] for r in all_results if r['filing_year'] == year and r['size'] == size]
            if len(vals) >= 5:
                size_year_data.append({'size': size, 'year': year, 'n': len(vals),
                                       'median': round(median(vals), 1),
                                       'p25': round(percentile(vals, 25), 1),
                                       'p75': round(percentile(vals, 75), 1)})

    # ── Summary stats ──
    summary = {
        'bis_count': len(bis_results),
        'now_count': len(now_results),
        'total': len(all_results),
        'bis_year_range': '2004-2019',
        'now_year_range': '2017-2025',
    }

    chart_data = {
        'summary': summary,
        'by_year': year_data,
        'by_borough_year': boro_year_data,
        'by_size_year': size_year_data,
    }

    path = os.path.join(DATA_DIR, 'chart_data.json')
    with open(path, 'w') as f:
        json.dump(chart_data, f, indent=2)
    print(f"\nExported chart data to {path}")

# ── Main ─────────────────────────────────────────────────────────

if __name__ == '__main__':
    # Legacy BIS system
    filings = pull_bis_filings()
    cos = pull_cos()
    bis_results = compute_timelines(filings, cos)

    # DOB NOW system
    now_filings = pull_dobnow_filings()
    now_results = compute_dobnow_timelines(now_filings)

    # Analyze BIS (primary, most complete)
    print("\n\n=== LEGACY BIS SYSTEM ===")
    analyze(bis_results)

    # Analyze DOB NOW
    print("\n\n=== DOB NOW SYSTEM ===")
    analyze(now_results)

    # Export
    export_csv(bis_results, 'timelines_bis.csv')
    export_csv(now_results, 'timelines_dobnow.csv')
    export_chart_data(bis_results, now_results)
