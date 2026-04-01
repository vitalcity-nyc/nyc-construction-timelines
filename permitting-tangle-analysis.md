# The NYC construction permitting tangle

An analysis of overlapping jurisdictions, contradictory requirements, and sequential bottlenecks in New York City's new construction permitting process.

---

## Part A: The regulatory landscape

### Agencies that touch a new building

A new residential construction project in New York City can require approvals, reviews, or sign-offs from **at least 11 city, state, and federal agencies**, depending on the project's location, size, and complexity. No single agency controls the full permitting path. The following agencies each hold independent authority over portions of the process:

| Agency | Authority | Legal basis | What they review |
|--------|-----------|-------------|-----------------|
| Department of Buildings (DOB) | Primary permitting authority | NYC Admin Code Title 28; NYC Building Code (2014, as amended) | Structural integrity, egress, zoning compliance, construction safety |
| Department of City Planning (DCP) | Zoning and land use | NYC Charter Ch. 8; NYC Zoning Resolution | Zoning text amendments, special permits, ULURP actions, environmental review |
| Fire Department (FDNY) | Fire safety | NYC Admin Code Title 29; 3 RCNY Ch. 9 | Fire protection plans, sprinkler systems, fire alarm systems, means of egress |
| Department of Environmental Protection (DEP) | Water and sewer | NYC Admin Code Title 24; 15 RCNY Ch. 31 | Sewer connections, stormwater management, water supply |
| Department of Transportation (DOT) | Streets and sidewalks | NYC Admin Code Title 19 | Street openings, sidewalk closures, crane permits, curb cuts |
| Landmarks Preservation Commission (LPC) | Historic preservation | NYC Admin Code Title 25, Ch. 3 | Any work on designated landmarks or within historic districts |
| Board of Standards and Appeals (BSA) | Variances and appeals | NYC Charter Ch. 27 | Zoning variances, special permits, appeals of DOB determinations |
| Housing Preservation and Development (HPD) | Affordable housing | NYC Admin Code Title 26; Housing Maintenance Code | Affordable housing compliance, inclusionary housing, 421-a/485-x certifications |
| Office of Environmental Coordination (OEC) | Environmental review | Executive Order 91 (1977); CEQR rules (43 RCNY Ch. 6) | City Environmental Quality Review (CEQR) for discretionary actions |
| Metropolitan Transportation Authority (MTA) | Transit adjacency | Public Authorities Law | Zoning for Accessibility easements, transit-adjacent construction review |
| New York State Department of Labor (DOL) | Asbestos and worker safety | Labor Law Art. 30 | Asbestos abatement permits for demolition and renovation |

Additional agencies may be involved depending on project specifics: the Office of Environmental Remediation (OER) for brownfield sites, the Army Corps of Engineers for waterfront projects, the Federal Aviation Administration (FAA) for buildings above certain heights near airports, and the State Department of Environmental Conservation (DEC) for wetland-adjacent sites.

### The permitting sequence

For a typical new residential building, the permitting process moves through eight stages. At each stage, one or more agencies must act before the project can advance:

**Stage 1: Pre-filing and zoning analysis**
- Developer determines whether the project conforms to the Zoning Resolution (ZR)
- If it conforms as-of-right: proceed directly to DOB filing
- If it requires a zoning change, special permit, or variance: ULURP process (DCP, City Planning Commission, Community Board, Borough President, City Council) -- adds 7-11 months minimum
- If in a historic district or on a landmark site: LPC review required before DOB filing

**Stage 2: Environmental review (if discretionary action required)**
- Type I actions (6 NYCRR 617.4): for NYC (population 1M+), residential projects of 1,000+ units; full Environmental Impact Statement (EIS) may be needed
- Type II actions: categorically exempt (most as-of-right projects). **Green Fast Track for Housing** (effective June 3, 2024) added NYC-specific Type II designations for residential projects up to 250 units meeting certain conditions, based on review of 500+ housing projects from 2013-2023
- Unlisted actions: Environmental Assessment Statement (EAS) required, which may lead to EIS
- CEQR process has no statutory deadline -- review duration depends on scope and lead agency
- Traffic analysis required under CEQR Technical Manual Ch. 16 if project generates 50+ vehicle trip ends per peak hour

**Stage 3: DOB plan filing**
- Licensed Professional Engineer (PE) or Registered Architect (RA) files plans via DOB NOW: Build
- Plans examined for compliance with Building Code, Zoning Resolution, and Multiple Dwelling Law
- Two pathways: (a) DOB plan examination, or (b) professional self-certification
- Self-certified plans bypass DOB review but are subject to quality assurance audit

**Stage 4: Plan examination and objections**
- DOB plan examiners review structural, egress, fire safety, and zoning compliance
- Objections issued if plans do not comply; applicant must respond and re-submit
- FDNY conducts concurrent (in theory) fire protection system review
- DEP reviews sewer connection and stormwater management plans (threshold: 20,000+ sq ft soil disturbance or 5,000+ sq ft new impervious surface)
- DOT reviews if project requires street opening, sidewalk shed, or crane operations

**Stage 5: Permit issuance**
- DOB issues work permits once all objections are resolved
- Permits valid for 2 years; expire if work not commenced within 12 months (Admin Code 28-105.4)
- Foundation permit may be issued separately from superstructure permit

**Stage 6: Construction and inspections**
- DOB conducts progress inspections at mandated milestones
- FDNY inspects fire protection system installation
- DOT issues crane and equipment permits as needed
- DEP inspects sewer connections and stormwater controls

**Stage 7: Certificate of Occupancy (CO)**
- Temporary Certificate of Occupancy (TCO) requires:
  - DOB sign-off on all required inspections
  - FDNY Letter of Approval (LOA) or fire alarm affidavit
  - DEP sign-off on sewer/water connections
  - All open violations resolved or deemed non-hazardous
- Final CO requires all outstanding items closed
- 637 NYC office buildings were operating without valid TCOs or final COs as of 2024 (NYC Comptroller)

**Stage 8: Post-occupancy compliance**
- Ongoing DOB compliance (facade inspections, boiler inspections, elevator inspections)
- HPD ongoing affordable housing monitoring (if applicable)
- LPC ongoing compliance for landmark buildings

---

## Part B: Overlap and contradiction inventory

### B.1 DOB vs. FDNY: parallel fire safety jurisdictions

**The overlap**: Both DOB and FDNY review fire safety aspects of new construction, but under different legal authorities and with different standards.

- DOB reviews egress, fire-rated construction, and fire protection system design under the NYC Building Code (2014)
- FDNY reviews the same fire protection systems under 3 RCNY Chapter 9 and NYC Fire Code
- DOB issues the construction permit; FDNY issues the Letter of Approval (LOA) required for TCO

**The tangle**: FDNY review is described as "concurrent" with DOB review but in practice is sequential. FDNY will not schedule a re-inspection until DOB has substantially approved the plans. The FDNY re-inspection appointment backlog runs approximately **7 weeks** as of 2024. This creates a forced wait at the end of construction -- the building is physically complete but cannot be occupied until FDNY scheduling catches up.

**Data evidence**: COs issued per year have dropped sharply even as construction activity has risen:
- 2019: 17,217 COs
- 2020: 15,250
- 2021: 6,158
- 2022: 3,439
- 2023: 2,662
- 2024: 1,737
- 2025 (partial): 1,377

This 90% decline from 2019 to 2024 reflects the cumulative effects of FDNY scheduling delays, DOB staffing reductions, and the incomplete migration to DOB NOW (which disrupted CO processing workflows).

### B.2 DOB vs. DCP: who owns zoning?

**The overlap**: Zoning compliance is reviewed by both DOB (for as-of-right projects) and DCP (for discretionary actions).

- DOB plan examiners check bulk, use, and parking compliance against the Zoning Resolution for every project filing
- DCP administers the ULURP process for zoning changes, special permits, and certifications
- BSA handles variance applications when neither as-of-right compliance nor a special permit is available

**The contradiction**: DOB interprets the Zoning Resolution for permitting purposes, but DCP writes the ZR. When the ZR is ambiguous -- which is frequent given its 5,000+ pages accumulated since 1961 -- DOB and DCP may interpret the same provision differently. Applicants sometimes receive DOB objections based on zoning interpretations that DCP's own guidance would not support, or vice versa. There is no formal reconciliation mechanism.

**City of Yes complication**: The December 2024 passage of City of Yes for Housing Opportunity amended numerous ZR provisions (parking requirements, ADU legalization, transit-oriented development bonuses). DOB plan examiners must now apply new ZR text that does not yet have full implementation rules. Until DOB's internal guidance manuals and DOB NOW's automated zoning check modules are updated, there is a gap between what the ZR now allows and what DOB's systems will approve.

### B.3 Self-certification: speed vs. accountability

**The system**: NYC Admin Code 28-104.2.1 allows licensed PEs and RAs to self-certify that their plans comply with all applicable codes, bypassing DOB plan examination. DOB is required to audit a random sample of self-certified applications within 45 days (Admin Code 28-104.2.1.1).

**The contradiction**:
- Self-certification was designed to reduce DOB backlogs and speed approvals for code-compliant projects
- But the NYC Comptroller's 2023 audit found DOB does not always conduct required audits within the 45-day timeframe
- DOB lacks formal guidelines for determining what constitutes a "serious" code violation during audits, leading to inconsistent enforcement across boroughs
- The DOB NOW system does not include a self-certification field, creating a data gap -- the city cannot systematically track how many current permits are self-certified

**Data gap**: The legacy BIS (Building Information System) recorded 1,716,858 self-certified permits. DOB NOW, which handles all new filings, has no equivalent tracking field. This means the city has no centralized data on what percentage of current construction is self-certified and cannot assess whether self-certification is producing more or fewer code violations than DOB-examined plans.

### B.4 Sequential dependencies that could be concurrent

Several agency reviews are structured sequentially even though the underlying work is independent:

| Review | Currently | Could be | Estimated time savings |
|--------|-----------|----------|----------------------|
| LPC review before DOB plan filing | Sequential | Concurrent with DOB plan exam | Median 14 days; P90 140 days |
| FDNY LOA before TCO | Sequential | Concurrent inspection scheduling | ~7 weeks |
| DEP sewer sign-off before CO | Sequential | Concurrent with final DOB inspection | Variable |
| DOT sidewalk/street permits | Separate from DOB timeline | Bundled or concurrent application | Variable |
| BSA variance hearing | Must precede DOB filing | Could run concurrent with preliminary plan prep | 4-6 months typical |

The LPC dependency is particularly significant: for the 10% of projects that take longest through LPC (P90 = 140 days, or ~4.7 months), this sequential requirement adds nearly half a year before DOB review even begins. For Certificate of Appropriateness applications (major alterations in historic districts), the median is 66 days and P90 is 222 days (7.4 months).

### B.5 Geographic regulatory boundaries

NYC's permitting requirements vary sharply across geographic boundaries that do not align with each other:

**Landmark districts**: 37,000+ properties in 157 historic districts (as of 2024) are subject to LPC review. LPC district boundaries were drawn on architectural/historical grounds and do not correspond to zoning district boundaries, community board boundaries, or DOB borough office jurisdictions.

**CEQR traffic analysis**: The CEQR Technical Manual Chapter 16 uses 60th Street in Manhattan as a dividing line for traffic modeling methodology. South of 60th Street, a 50% taxi overlap assumption is applied (reflecting higher taxi density). North of 60th Street, only 25% overlap is assumed. This arbitrary geographic boundary means an identical project at 59th Street and 61st Street faces different environmental review standards.

**Flood zones**: Projects in FEMA flood zones (Zones A, AE, VE, and the Shaded X Zone) must comply with Appendix G of the NYC Building Code, which requires elevated construction, flood-resistant materials, and additional DEP review. The flood zone map was last comprehensively updated in 2013 (effective 2024 PFIRM maps are under appeal). Flood zone boundaries do not align with zoning districts, creating situations where a single zoning lot straddles two different flood risk categories with different construction requirements.

**Coastal zones**: The NYC Waterfront Revitalization Program (WRP) applies additional review requirements for projects in the designated coastal zone boundary. WRP review is conducted by DCP and must be completed before CEQR sign-off. The coastal zone boundary is distinct from FEMA flood zones, so a project can be in one, both, or neither.

### B.6 Code vintage conflicts

NYC's building regulatory framework draws from laws written across different eras, and they have not been reconciled:

**Multiple Dwelling Law (1929)**: NYS law that still governs basic requirements for apartment buildings, including the live-in superintendent rule (Section 83, threshold: 9+ units, or 13+ if owner does not reside), egress requirements (Section 187), and lot coverage rules. The MDL was written for tenement-era conditions and has been amended piecemeal but never comprehensively rewritten.

**NYC Building Code (2014)**: Comprehensive rewrite of the 1968 Building Code, incorporating International Building Code (IBC) standards. But the 2014 code was itself amended by the 2022 code update, which changed egress, fire safety, and accessibility provisions. Projects that filed plans under the 1968 code and are still in construction face a different set of requirements than those filing under the 2014 code.

**Zoning Resolution (1961, as amended)**: The ZR has been continuously amended for 65 years. City of Yes for Housing Opportunity (December 2024) is the most recent major amendment. The ZR's layered amendments create situations where the parking requirements in one section of the ZR were written assuming land use patterns that another section of the ZR has since changed.

**The contradiction**: The MDL requires two independent means of egress for most multifamily buildings (Section 187), but allows a single means with a sprinkler system. The Building Code (Section 1006.3.2 and Table 1006.3.2) allows single exit up to **6 stories** for R-2 occupancy with sprinklers, with a 2,000 sq ft per story floor area cap. These two standards coexist in different legal authorities. The Building Code provision is more permissive than commonly understood, but the MDL's sprinkler exception and the Building Code's table interact in ways that require careful reconciliation for each specific project configuration.

### B.7 Elevator requirements: NYC vs. everywhere else

NYC Building Code Section 3002.4 requires buildings of 5 or more stories (or 4 or more stories below grade) to provide at least one elevator. Section 3002.4.2 further requires at least one **stretcher-sized elevator** -- large enough to accommodate a 24" x 84" ambulance stretcher in a horizontal, open position -- in these buildings.

**The tangle**: The stretcher-size requirement is distinctive to NYC among major US cities. It increases elevator shaft dimensions, which reduces usable floor area on every floor. For narrow-lot buildings common in Brooklyn and Queens, a stretcher-sized elevator shaft can reduce the buildable unit count by 1-2 units per floor. Over a 6-story building, this represents 6-12 fewer units -- a significant impact on project economics and housing supply.

The requirement interacts with single-stair proposals: allowing single-stair buildings above 3 stories would be partially offset if the stretcher elevator requirement remains, because the space saved by eliminating a second stairway may be consumed by the larger elevator shaft.

### B.8 The live-in superintendent mandate

Multiple Dwelling Law Section 83 requires a resident superintendent (or janitor) for any building with **13 or more families** where the owner does not reside in the building. The superintendent must live in the building or within 200 feet.

**The tangle**: This 1929 rule was written for an era when building systems were manually operated (coal boilers, hand-operated elevators). Modern building systems are automated and remotely monitored. The requirement forces developers of buildings with 13+ units to either:
- Dedicate a residential unit to the superintendent (reducing rentable/saleable units)
- Have the owner reside in the building (impractical for institutional developers)
- House the superintendent within 200 feet (requiring a second property or arrangement)

For a 12-unit building -- common in the City of Yes density bonuses for transit-adjacent lots -- the superintendent unit represents 8% of total units removed from the housing supply. The MDL threshold has not been adjusted since 1929, despite the transformation of building management technology.

---

## Part C: Data-driven evidence

### C.1 New building permit processing times

**Source**: DOB NOW: Build job filings (Socrata `w9ak-ipjd`), 20,870 New Building filings, 2024-present.

The median time from filing to first permit issuance for a new building is **108 days (3.6 months)**. At the 90th percentile, it takes **280 days (9.3 months)**. At the 95th percentile: **329 days (nearly 11 months)**.

| Metric | Days | Months |
|--------|------|--------|
| P25 (fastest quarter) | 39 | 1.3 |
| Median | 108 | 3.6 |
| Mean | 127 | 4.2 |
| P75 | 195 | 6.5 |
| P90 | 280 | 9.3 |
| P95 | 329 | 11.0 |

**By borough**: Manhattan is the slowest jurisdiction at a median of 133 days. Staten Island is the fastest at 33 days -- a 4x difference for the same permit type reviewed by the same agency under the same code.

| Borough | Median days | Records |
|---------|-------------|---------|
| Manhattan | 133 | 182 |
| Bronx | 132 | 905 |
| Brooklyn | 129 | 1,243 |
| Queens | 124 | 1,056 |
| Staten Island | 33 | 964 |

The Manhattan-Staten Island gap reflects several compounding factors: higher complexity of Manhattan projects, more frequent landmark district involvement, more frequent CEQR triggers, and differing DOB borough office staffing levels.

### C.2 Alteration permit processing times

**Source**: DOB NOW: Build job filings, 50,000 Alteration filings, 2025-2026.

Alterations are significantly faster than new buildings: median **10 days** from filing to first permit, P90 of **62 days**.

| Metric | Days |
|--------|------|
| Median | 10 |
| Mean | 22 |
| P75 | 30 |
| P90 | 62 |
| P95 | 84 |

The 10x difference between alteration median (10 days) and new building median (108 days) reflects the heavier review burden for new construction: full structural review, full zoning review, FDNY plan review, and more frequent DEP/DOT involvement.

### C.3 Objection rates

14.7% of new building filings have current status of "Objections" -- meaning DOB has found code or zoning violations in the submitted plans that must be corrected before approval. For alterations, the objection rate is 5.1%.

Of 20,870 New Building filings:
- 10,877 (52%) approved
- 3,375 (16%) permit issued for entire job
- 3,075 (15%) stuck at objections
- 1,426 (7%) in plan examiner review
- 681 (3%) withdrawn

The 15% objection rate for new buildings means roughly 1 in 7 projects hits a regulatory wall during plan review. Each objection cycle -- DOB issues objections, applicant responds, DOB re-reviews -- adds weeks to months to the timeline.

### C.4 LPC processing times

**Source**: LPC Permit Application Information (Socrata `dpm2-m9mq`), 50,000 applications, 2021-present.

| Regulation type | Records | Median days | P90 days |
|----------------|---------|-------------|----------|
| Expedited Certificate of No Effect | 6,638 | 1 | 3 |
| Authorization to Proceed | 703 | 9 | 58 |
| Notice of Compliance | 2,961 | 10 | 83 |
| Certificate of No Effect | 19,940 | 17 | 106 |
| Permit for Minor Work | 7,158 | 17 | 101 |
| Miscellaneous - Amendment | 5,158 | 22 | 120 |
| Certificate of Appropriateness | 966 | 66 | 222 |

For major projects requiring a Certificate of Appropriateness (CoA) -- the approval type for significant alterations to landmarks or new construction in historic districts -- median processing is **66 days** with a P90 of **222 days (7.4 months)**. Since LPC review must typically be completed before DOB plan filing, this sequential dependency alone adds 2-7 months to the timeline for projects in historic districts.

LPC application volume has been steady at approximately 11,000-12,000 per year (2022-2025), with the LPC public hearing schedule among the busiest of any city agency: 250 City Record entries for public hearings since 2022.

### C.5 Demolition processing times

Demolition permits -- which precede new construction on sites with existing structures -- take a median of **81 days**, P75 of **146 days**, and P90 of **224 days**. These timelines are in addition to the new building permit timeline, since demolition and new building permits are filed separately.

### C.6 Filing volumes vs. staffing

New Building filings have surged:
- 2024: 2,559 filings
- 2025: 13,337 filings (5.2x increase)

Meanwhile, DOB construction staff declined from 662 (March 2021) to 519 (March 2024), a 21.6% reduction. The 5x increase in filings against a 21% staffing decline explains lengthening processing times.

### C.7 Certificate of Occupancy decline

CO issuance has dropped precipitously:

| Year | COs issued |
|------|-----------|
| 2019 | 17,217 |
| 2020 | 15,250 |
| 2021 | 6,158 |
| 2022 | 3,439 |
| 2023 | 2,662 |
| 2024 | 1,737 |

The 90% decline from 2019 to 2024 is not driven by a corresponding decline in construction activity -- filing volumes have increased. It reflects the compounding effects of:
- DOB NOW migration disruptions (2020-2022)
- FDNY re-inspection backlogs (~7 weeks)
- Staffing reductions at DOB
- Increased violation closeout requirements

### C.8 Bottom 20 districts: housing production concentration

**Source**: NYC Housing Database (Socrata `hg8x-zxpr`), 5,437 projects, 2019-present.

Housing production is heavily concentrated in a small number of community boards. The bottom 20 districts by total affordable units produced since 2019:

| District | Borough | Units |
|----------|---------|-------|
| BX-205 | Bronx | 35 |
| QN-10 | Queens | 37 |
| QN-13 | Queens | 56 |
| QN-11 | Queens | 76 |
| SI-02 | Staten Island | 117 |
| BK-11 | Brooklyn | 274 |
| BK-18 | Brooklyn | 278 |
| QN-05 | Queens | 295 |
| BK-12 | Brooklyn | 358 |
| QN-03 | Queens | 387 |

Compare with the top 5: BX-10 (15,685 units), BX-04 (10,627), BK-05 (10,117), QN-12 (9,426), MN-11 (7,469).

The bottom 20 districts collectively produced fewer units than the single top-producing district (BX-10). These low-producing districts are disproportionately in eastern Queens, Staten Island, and southern Brooklyn -- areas with restrictive zoning (R1-R3 residential districts) that limits density to 1-2 family homes.

### C.9 Complaint-driven enforcement

DOB relies heavily on 311 complaints to trigger enforcement:
- 50,000 complaints analyzed (2022-present)
- Median complaint resolution time: 16 days
- Mean: 80 days
- P90: 167 days

The reactive complaint system means enforcement activity is distributed based on who files complaints, not where violations are most prevalent. Communities with more organized civic groups or higher awareness of 311 file more complaints and receive more enforcement attention.

### C.10 City Record hearing volumes

Construction-related agencies with the most public hearing entries since 2022:

| Agency | Hearing entries |
|--------|----------------|
| Landmarks Preservation Commission | 250 |
| Housing Preservation and Development | 229 |
| Transportation | 156 |
| Board of Standards and Appeals | 98 |
| City Planning Commission | 93 |
| Environmental Protection | 51 |
| Fire Department | 5 |
| Buildings | 1 |

The disparity is striking: LPC holds 250 public hearings while DOB holds 1. This reflects the different decision-making structures -- DOB operates through administrative plan review while LPC operates through a quasi-judicial commission -- but it also means LPC-regulated projects face a public hearing calendar bottleneck that DOB-only projects do not.

---

## Part D: The 11 reform proposals in regulatory context

### D.1 Enforce maximum permitting periods

**Current law**: Admin Code 28-104.2.7 requires the DOB commissioner to approve or reject completed construction documents within **40 calendar days**, with an optional 20-day extension for good cause. Admin Code 28-105.4 sets permit validity (expire after 2 years, or 12 months without commencement). DOB also publishes operational service level targets (10 business days for NB/A1 first status).

**The gap**: The 40-day statutory deadline has no enforcement mechanism -- no deemed-approval provision, no penalty for non-compliance, no applicant remedy. The median new building processing time is 108 days, or 2.7x the statutory limit. When filing volumes surge (as in 2025's 5x increase in NB filings) and staffing is cut (21% since 2021), the already-unenforced deadline becomes even more aspirational.

**What the data shows**: Median new building processing time is 108 days (3.6 months). At P90, it reaches 280 days. These timelines do not include pre-filing activities (LPC review, environmental review, BSA hearings) or post-permit activities (FDNY LOA for CO).

**Regulatory tangles exposed**: Mandatory review periods would need to cover not just DOB but also FDNY (fire plan review), DEP (sewer/stormwater), DOT (street/sidewalk), and LPC (landmarks). A DOB-only mandate would simply push bottlenecks to other agencies.

### D.2 Clean up the FDNY Certificate of Occupancy process

**Current law**: FDNY issues Letters of Approval (LOA) required before DOB can issue a TCO. The LOA confirms that fire protection systems (sprinklers, fire alarms, standpipe) are installed per approved plans.

**The tangle**: Two approval pathways exist:
1. FDNY re-inspection: 7-week appointment backlog
2. Fire alarm affidavit: faster alternative where a licensed professional certifies the installation

The affidavit path is faster but less commonly used. The re-inspection path creates a structural bottleneck at the end of construction.

**What the data shows**: The 90% decline in COs issued (17,217 in 2019 to 1,737 in 2024) indicates systematic failure in the CO pipeline. The NYC Comptroller found 637 office buildings operating without valid COs and 88 with immediately hazardous violations.

### D.3 Loosen rules around elevator size and capacity

**Current law**: NYC Building Code 3002.4 requires elevators in buildings of 5+ stories. Section 3002.4.2 requires at least one stretcher-sized elevator (accommodating a 24" x 84" ambulance stretcher).

**The tangle**: The stretcher requirement is unique to NYC and increases elevator shaft dimensions significantly. On narrow lots (25-foot frontage buildings common in Brooklyn and Queens), the oversized shaft consumes floor area that could otherwise contain 1-2 additional units per floor. Across a 6-story building, this is 6-12 potential units lost.

**Interaction with other proposals**: Single-stair reform (D.5) would free floor area currently dedicated to a second stairway. But if the elevator requirement remains at its current size, the net space gain from single-stair is partially consumed by the elevator shaft. The two reforms are interdependent.

### D.4 Reconsider the live-in super rule

**Current law**: Multiple Dwelling Law Section 83 requires a resident superintendent for buildings with **13 or more families** where the owner does not reside. The superintendent must live in the building or within 200 feet. Where 2-3 multiple dwellings are connected or adjoining, one resident janitor is sufficient.

**The tangle**: The MDL was written in 1929 for buildings with coal-fired boilers and manual systems. Modern buildings have automated HVAC, electronic access control, and remote monitoring. The 13-unit threshold has not been adjusted, despite changes in building technology.

**What the data shows**: City of Yes density bonuses will produce more 13-20 unit buildings on lots previously zoned for lower density. Each of these buildings will need a superintendent unit, reducing the housing supply gain from the density bonus by approximately 5-8%.

**State vs. city conflict**: The MDL is state law. NYC cannot unilaterally change it. Reform requires action by the New York State Legislature, adding a political dimension beyond city control.

### D.5 Single stairs and flexible floor plates

**Current law**: Multiple Dwelling Law Section 187 requires two independent means of egress for most multifamily buildings, but allows a single means with a sprinkler system. NYC Building Code Section 1006.3.2 and Table 1006.3.2 allow single exit for R-2 occupancy (apartments) with sprinklers up to **6 stories**, with a **2,000 sq ft per story** floor area cap.

**The tangle**: The Building Code already permits single-stair buildings taller than commonly understood -- up to 6 stories with the floor area limit. But the 2,000 sq ft cap severely constrains the building footprint, making it viable only on very small lots. The MDL's sprinkler exception and the Building Code's table interact in ways that require careful reconciliation. Expanding the floor area cap or height limit would require amending both the city Building Code and potentially the state MDL, since the MDL is the more restrictive authority for larger floor plates.

**National context**: As of 2025, seven states (Colorado, Montana, New Hampshire, Texas, Maine, Hawaii, Maryland) have advanced single-stair reforms. A Pew Charitable Trusts study (February 2025) found that small single-stairway apartment buildings have a strong safety record. NYC Council introduced Int 0794-2022 to expand single-stair allowances, but it has not passed.

**Interaction with other proposals**: Single-stair reform interacts with elevator requirements (D.3) and the live-in super rule (D.4). All three affect the internal layout and unit count of mid-rise residential buildings.

### D.6 Scrap traffic analyses below 60th Street

**Current law**: CEQR Technical Manual Chapter 16 requires traffic analysis for projects generating 50+ vehicle trip ends per peak hour. The Manual uses 60th Street in Manhattan as a methodological dividing line: south of 60th Street, a 50% taxi overlap assumption applies; north of 60th Street, 25%.

**The tangle**: The 60th Street line is a traffic modeling assumption, not a statutory boundary. But it has regulatory force because CEQR determinations based on the Technical Manual are required for discretionary land use approvals. An identical project at 59th Street and 61st Street faces different traffic modeling parameters.

**The broader issue**: Below 60th Street, Manhattan has among the lowest car ownership rates in the United States. The transit mode share exceeds 70%. Requiring traffic analysis for residential projects in an area where most residents do not own cars adds months to environmental review timelines for projects that will generate minimal vehicle traffic.

**What the data shows**: 443 ULURP projects in the dataset are Type I actions requiring full environmental assessment. An unknown fraction of these include traffic analyses below 60th Street.

### D.7 Point persons in City Hall for major projects

**Current system**: No formal "construction czar" or dedicated ombudsman exists for private development projects. The Deputy Mayor for Operations oversees infrastructure agencies. DDC's Community Construction Liaison (CCL) program handles community inquiries about construction impacts (700+ inquiries in 2024) but is focused on public projects.

**The tangle**: A major private construction project may require simultaneous approvals from DOB, FDNY, DEP, DOT, LPC, and potentially DCP/BSA. Each agency operates on its own timeline with its own application system. No single point of contact has authority to coordinate across agencies or resolve inter-agency conflicts.

### D.8 Staff up offices essential to construction approvals

**What the data shows**: DOB construction staff fell from 662 to 519 between March 2021 and March 2024 (21.6% decline). During the same period, New Building filings surged from approximately 2,500 to 13,300 per year (5.2x increase). The staffing-to-filing ratio has deteriorated by roughly 6.6x.

LPC staffing is also under scrutiny: the NYC Council Committee on Land Use scheduled a hearing on LPC staffing levels and vacancy details for March 11, 2025.

**The tangle**: Staffing levels are set through the city budget process (OMB and City Council), not by the agencies themselves. DOB cannot hire more plan examiners without budgetary approval. This creates a structural disconnect between workload (driven by private market activity) and capacity (driven by political budget priorities).

### D.9 Expedite rules-making for ballot referenda

**Current law**: The City Administrative Procedure Act (CAPA, NYC Charter Chapter 45) requires a minimum 30-day public comment period between rule proposal and public hearing. Typical timeline: 75-90 days from rule publication to final adoption.

**The tangle**: The 2024 ballot referenda and the 2025 Charter Revision Commission proposals (5 ballot proposals adopted) require implementing rules from multiple agencies. Each agency must independently conduct CAPA-compliant rulemaking. The 30-day minimum is statutory and cannot be shortened without charter amendment.

**What this means**: Even after voters approve reforms, implementation is delayed by months of agency rulemaking. The cumulative effect of multiple agencies each conducting 75-90 day rulemaking processes is that voter-approved reforms may not take effect for 6-12 months after the election.

### D.10 Bottom 20 districts housing plans

**What the data shows**: The bottom 20 community districts by affordable housing production since 2019 are concentrated in eastern Queens (QN-10, QN-11, QN-13), Staten Island (SI-02), and southern Brooklyn (BK-11, BK-18). These districts collectively produced fewer affordable units (approximately 2,100) than a single top-producing district (BX-10 at 15,685 units).

**The tangle**: Low-producing districts typically have restrictive zoning (R1-R3) that limits density. City of Yes loosened some restrictions (ADUs, transit-oriented development), but the lowest-density zones received the most modest upzones. The 485-x tax incentive is designed to incentivize affordable housing in these areas, but its interaction with restrictive zoning means the density bonus may be insufficient to make projects financially viable on low-density lots.

**Geographic disparity**: The top 10 housing-producing districts have an average median income of $61,969; the bottom 10 average $87,033. Lower-income, majority-Black and Hispanic neighborhoods are absorbing the majority of new construction while higher-income neighborhoods contribute minimally.

### D.11 Zoning for Accessibility (ZFA) density bonus

**Current law**: ZFA was adopted October 7, 2021. It provides up to a 20% floor area ratio (FAR) bonus for developers who fund or construct transit accessibility improvements (primarily elevators) at MTA stations within 500 feet (or 1,500 feet in central business districts).

**The tangle**: ZFA requires coordination between three agencies -- DCP (zoning), MTA (transit), and DOB (building permits) -- each operating under different legal authorities (ZR, Public Authorities Law, Building Code). The density bonus is only useful on sites near stations that MTA has identified as priority accessibility projects, limiting its geographic reach.

**What the data shows**: Two ZFA-funded elevators are in progress (Queensboro Plaza, Q1 2025; 57th Street N/R/W, Q1 2026). The slow pace of implementation -- two elevators in four years -- reflects the complexity of three-agency coordination.

**Expansion considerations**: Increasing the FAR bonus beyond 20% or expanding the distance threshold beyond 500 feet would increase the number of eligible sites. But each expansion also increases the number of agency coordination points and the complexity of the zoning analysis required by DOB plan examiners.

---

## Summary of findings

The NYC construction permitting system is not a single process but an overlay of **at least 11 independent agency jurisdictions** operating under **different legal authorities from different eras** (1929 MDL, 1961 ZR, 2014 Building Code, 2024 City of Yes amendments).

The data reveals three structural problems:

1. **Sequential bottlenecks**: Reviews that could run concurrently are instead sequential, with each step waiting for the previous one. LPC before DOB before FDNY creates a chain where the total timeline is the sum of all reviews, not the maximum.

2. **Staffing-workload mismatch**: DOB filings surged 5x while staffing fell 21%, producing a 6.6x deterioration in the staffing-to-filing ratio. CO issuance has dropped 90% from 2019 levels.

3. **Code archaeology**: Requirements from 1929 (live-in super), 1961 (base zoning), and 2014 (building code) coexist without reconciliation. Reform proposals must navigate city law, state law, and the city charter simultaneously.

The 11 reform proposals address real problems documented in the data. But many of them interact with each other (single stairs + elevators + live-in super all affect the same floor plate), and several require state legislative action (MDL amendments for single stairs and live-in super) that the city cannot accomplish unilaterally.
