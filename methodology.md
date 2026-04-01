# Methodology: NYC permitting tangle analysis

## Overview

This analysis maps the regulatory overlaps, contradictions, and sequential bottlenecks in New York City's new construction permitting process. It combines regulatory text analysis (tracing legal authorities across 11+ agencies) with quantitative analysis of NYC Open Data.

## Data sources

All data was pulled from NYC Open Data Socrata APIs on April 1, 2026.

| Dataset | Socrata ID | Endpoint | Records | Date filter | Fields used |
|---------|-----------|----------|---------|-------------|-------------|
| DOB NOW: Build job filings (New Building) | w9ak-ipjd | `data.cityofnewyork.us/resource/w9ak-ipjd.json` | 20,870 | job_type = 'New Building' | job_filing_number, filing_status, borough, job_type, filing_date, first_permit_date, proposed_dwelling_units |
| DOB NOW: Build job filings (Alteration) | w9ak-ipjd | same | 50,000 | job_type = 'Alteration', filing_date > 2019-01-01 | Same fields |
| DOB Certificates of Occupancy | bs8b-p36w | `data.cityofnewyork.us/resource/bs8b-p36w.json` | 48,127 | job_type in (NB, A1), c_o_issue_date > 2019-01-01 | job_number, job_type, c_o_issue_date, borough, issue_type |
| DOB complaints | eabe-havv | `data.cityofnewyork.us/resource/eabe-havv.json` | 50,000 | date_entered > 01/01/2022 | complaint_number, status, date_entered, complaint_category, disposition_date |
| DOB violations | 3h2n-5cm9 | `data.cityofnewyork.us/resource/3h2n-5cm9.json` | 50,000 | issue_date > 20220101 | violation_type, violation_category, issue_date |
| LPC permit applications | dpm2-m9mq | `data.cityofnewyork.us/resource/dpm2-m9mq.json` | 50,000 | received_date > 2019-01-01 | docket, received_date, regulation_type, issue_date, borough |
| ULURP/land use applications | hgx4-8ukb | `data.cityofnewyork.us/resource/hgx4-8ukb.json` | 10,000 | All available | project_id, ceqr_type, current_milestone, borough, actions |
| NYC Housing Database | hg8x-zxpr | `data.cityofnewyork.us/resource/hg8x-zxpr.json` | 5,437 | project_start_date > 2019-01-01 | project_id, borough, community_board, reporting_construction_type, all_counted_units |
| City Record (hearings/rules) | dg92-zbpx | `data.cityofnewyork.us/resource/dg92-zbpx.json` | 6,126 | section_name in (Public Hearings and Meetings, Rules, Special Materials), start_date > 2022-01-01 | agency_name, section_name, short_title, start_date |

## Calculations

### Processing times

**DOB permit processing time**: Calculated as `first_permit_date - filing_date` (calendar days) for each record where both fields are non-null and `first_permit_date > filing_date`. Records with processing times exceeding 3,650 days (10 years) were excluded as likely data errors.

**LPC processing time**: Calculated as `issue_date - received_date` (calendar days) with the same exclusion criteria.

Percentiles (P25, median, P75, P90, P95) were calculated from the sorted distribution of valid processing times. Mean was calculated as the arithmetic average.

### CO issuance counts

Annual counts based on the `c_o_issue_date` field, grouped by year. Includes both Temporary COs and Final COs (distinguished by `issue_type` field).

### Objection rates

Percentage of filings with `filing_status` beginning with "Objection" (case-insensitive), calculated as: objection count / total filings * 100.

### Bottom 20 districts

Community board unit totals calculated by summing `all_counted_units` for all records grouped by `community_board`. Ranked ascending; bottom 20 = 20 districts with the fewest total units.

### Staffing figures

DOB staffing data (662 in March 2021, 519 in March 2024) is from the New York State Comptroller's Construction Jobs Report (Report 8-2026) and industry sources. These are not from Open Data APIs.

### City Record agency counts

Count of records per `agency_name` where the agency name contains the target string (case-insensitive match). "Construction-related" agencies were manually selected: Buildings, City Planning Commission, Environmental Protection, Fire Department, Landmarks Preservation Commission, Transportation, Board of Standards and Appeals, Housing Preservation and Development.

## Regulatory text sources

| Authority | Citation | Used for |
|-----------|----------|----------|
| NYC Administrative Code Title 28 | Buildings | Permit validity (28-105.4), self-certification (28-104.2.1), plan examination, CO requirements |
| NYC Building Code (2014, as amended) | Local Law | Egress (Ch. 10), elevators (3002.4), fire protection (Ch. 9), construction safeguards |
| NYC Zoning Resolution | ZR Articles I-XIV | Bulk, use, parking, City of Yes amendments |
| Multiple Dwelling Law (NYS) | MDL | Egress (Section 187), superintendent requirement (Section 83) |
| CEQR Technical Manual (2025) | OEC | Environmental review thresholds, traffic analysis methodology (Ch. 16) |
| NYC Charter | Chapters 8, 26, 27, 45 | City Planning (Ch. 8), DOB (Ch. 26), BSA (Ch. 27), CAPA rulemaking (Ch. 45) |
| NYC Admin Code Title 29 | Fire Code | FDNY jurisdiction over fire protection systems |
| 3 RCNY Chapter 9 | FDNY rules | Fire protection plan review, Letter of Approval process |
| NYC Admin Code Title 24 | Environmental Protection | DEP sewer/stormwater jurisdiction |
| NYC Admin Code Title 25, Ch. 3 | Landmarks | LPC regulatory authority over landmark sites and historic districts |
| NYC Admin Code Title 19 | Transportation | DOT street opening, sidewalk, crane permit authority |
| Executive Order 91 (1977) | CEQR | Establishes City Environmental Quality Review process |
| 43 RCNY Chapter 6 | CEQR rules | CEQR procedural requirements |
| Public Authorities Law | NYS | MTA authority, Zoning for Accessibility legal basis |
| Labor Law Art. 30 | NYS | Asbestos abatement permits (DOL) |

## Limitations

1. **DOB NOW migration**: The transition from the legacy BIS (Building Information System) to DOB NOW (~2020-2022) created a break in the time series. Pre-2020 data uses different field structures and is not directly comparable. The analysis uses DOB NOW data (2024-present for NB, 2025-present for alterations) to avoid this discontinuity.

2. **50,000-record API limit**: Socrata API queries are capped at 50,000 records per request. For datasets with more records, the most recent 50,000 were retrieved. This means the analysis may not capture the full universe of older filings.

3. **FDNY data gap**: FDNY plan review and re-inspection timelines have no public dataset. The 7-week re-inspection backlog figure comes from industry reports and the NYC Comptroller's office, not from Open Data.

4. **Self-certification tracking**: DOB NOW lacks a self-certification field. The 1.7 million self-certified permits figure comes from the legacy BIS system. It is not possible to determine what percentage of current DOB NOW filings are self-certified.

5. **Inter-agency timing**: Processing times measure individual agency review periods (e.g., DOB filing-to-permit, LPC received-to-issued). The total end-to-end permitting timeline -- from initial concept to Certificate of Occupancy -- cannot be computed from these datasets because the datasets do not share a common project identifier that spans all agencies.

6. **CO data interpretation**: The steep decline in CO issuance (2019-2024) may partially reflect changes in data reporting practices during the DOB NOW migration, not solely operational delays. The magnitude of the decline (90%) exceeds what reporting changes alone would explain, but the exact contribution of each factor cannot be disaggregated.

7. **ULURP completeness**: The ULURP dataset contains 10,000 records without clear date filtering, making it difficult to compute processing timelines. Many records lack milestone dates.

8. **Staffing data**: Agency staffing figures are not available through NYC Open Data. The figures cited (DOB, LPC) come from state comptroller reports, city council hearing materials, and industry sources. Current vacancy rates are not publicly available for most agencies.

## Reproducibility

All API queries can be replicated using the Socrata endpoints and filters listed in the data sources table above. The Python analysis script (`analyze.py`) documents the exact computation methods for all derived statistics. Raw data files are stored in the `/data` directory.
