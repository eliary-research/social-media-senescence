# meta_quarterly.csv — Data Sources & Methodology

## Primary Sources

All Facebook DAU/MAU figures originate from Meta Platforms' SEC filings:
- **10-K Annual Reports** (filed February each year): contain Q4 and full-year figures
- **10-Q Quarterly Reports** (filed ~40 days after quarter end): contain quarterly figures
- **Earnings Press Releases** on investor.atmeta.com (formerly investor.fb.com)
- **Earnings Presentation Slides** (PDF): contain quarterly charts with exact figures

### SEC EDGAR Filing Links
- All Meta filings: https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001326801&type=10-&dateb=&owner=include&count=40
- Meta Investor Relations: https://investor.atmeta.com/financials/

### Specific Filings Referenced
| Period | Filing | URL |
|--------|--------|-----|
| 2012 10-K | FB-12.31.2012-10K | https://www.sec.gov/Archives/edgar/data/1326801/000132680113000003/fb-12312012x10k.htm |
| 2013 10-K | FB-12.31.2013-10K | https://www.sec.gov/Archives/edgar/data/1326801/000132680114000007/fb-12312013x10k.htm |
| 2014 10-K | FB-12.31.2014-10K | https://www.sec.gov/Archives/edgar/data/1326801/000132680115000006/fb-12312014x10k.htm |
| 2016 10-K | FB-12.31.2016-10K | https://www.sec.gov/Archives/edgar/data/1326801/000132680117000007/fb-12312016x10k.htm |
| 2017 10-K | FB-12.31.2017-10K | https://www.sec.gov/Archives/edgar/data/1326801/000132680118000009/fb-12312017x10k.htm |
| Q4 2018 Earnings | Slides PDF | https://s21.q4cdn.com/399680738/files/doc_financials/2018/Q4/Q4-2018-Earnings-Presentation.pdf |
| Q4 2019 Earnings | Slides PDF | https://s21.q4cdn.com/399680738/files/doc_financials/2019/q4/Q4-2019-Earnings-Presentation-_final.pdf |
| Q1 2021 Earnings | Slides PDF | https://s21.q4cdn.com/399680738/files/doc_financials/2021/FB-Earnings-Presentation-Q1-2021.pdf |
| Q4 2023 Earnings | Slides PDF | https://s21.q4cdn.com/399680738/files/doc_financials/2023/q4/Earnings-Presentation-Q4-2023.pdf |
| Q1 2024 Earnings | Slides PDF | https://s21.q4cdn.com/399680738/files/doc_financials/2024/q1/Earnings-Presentation-Q1-2024.pdf |
| Q4 2024 Earnings | Slides PDF | https://s21.q4cdn.com/399680738/files/doc_financials/2024/q4/Earnings-Presentation-Q4-2024.pdf |

### Secondary Sources (cross-reference / compilation)
- MacroTrends: https://www.macrotrends.net/stocks/charts/META/meta-platforms/revenue
- StockAnalysis: https://stockanalysis.com/stocks/meta/metrics/daily-active-users/
- Backlinko: https://backlinko.com/facebook-users
- Business of Apps: https://www.businessofapps.com/data/facebook-statistics/
- DemandSage: https://www.demandsage.com/facebook-statistics/

## Column Definitions

| Column | Definition | Source |
|--------|-----------|--------|
| `year` | Calendar year | — |
| `quarter` | Q1 (Jan-Mar), Q2 (Apr-Jun), Q3 (Jul-Sep), Q4 (Oct-Dec) | — |
| `platform` | `facebook` = Facebook app + Messenger (excludes Instagram, WhatsApp) | Meta SEC filings |
| `dau_millions` | Daily Active Users in millions, average for last month of quarter | Meta 10-K/10-Q |
| `mau_millions` | Monthly Active Users in millions, as of last day of quarter | Meta 10-K/10-Q |
| `dau_mau_ratio` | DAU / MAU (engagement stickiness metric) | Calculated |
| `revenue_billions` | Total Meta (formerly Facebook Inc.) revenue in USD billions | Meta 10-K/10-Q |
| `arpu_dollars` | Average Revenue Per User = revenue / avg(MAU_start, MAU_end) in USD | Meta reports + calculated |

## Important Caveats

### 1. Revenue is Company-Wide, Not Facebook-Only
Meta does not break out revenue by individual app. `revenue_billions` and `arpu_dollars` include
revenue from Instagram, WhatsApp Business, Audience Network, and other sources. For the EN1
senescence analysis, this is acceptable because:
- Facebook was the dominant revenue driver through ~2019
- The revenue trajectory still illustrates the advertising ratchet mechanism
- ARPU trend (up even as engagement quality declines) supports the senescence thesis

### 2. Q3 2018 Methodology Change
In Q3 2018, Meta updated its DAU/MAU calculation methodology to exclude certain data signals
previously misclassified as user activity. This reduced reported figures slightly. The pre-Q3-2018
figures are as-reported at the time (not retroactively adjusted).

### 3. Q4 2021: First-Ever DAU Decline
Q4 2021 reported 1,929M DAU vs Q3 2021's 1,930M — the first sequential decline in Facebook's
history. This is a key data point for the senescence argument.

### 4. 2024-2025 Data Precision
For 2024 Q2-Q4 and 2025 quarters, Meta increasingly emphasized "Family of Apps" metrics
(DAP/MAP) over Facebook-only figures. Facebook-only DAU/MAU for these later quarters are
derived from earnings reports where available, supplemented by analyst estimates and
third-party compilations. These figures carry somewhat lower precision than 2012-2023 data
and should be flagged in the paper.

### 5. Instagram Data
Meta has NEVER disclosed Instagram-only DAU or MAU in SEC filings. Instagram user counts
cited in media (e.g., "2 billion MAU") come from:
- Meta's own blog posts / press events (not SEC filings)
- Third-party estimates (Sensor Tower, data.ai, DataReportal)

For the EN1 paper, Instagram data is secondary. If needed, DataReportal annual estimates
can be used with appropriate caveats.

## Key Observations for EN1

1. **DAU/MAU ratio**: Rose from 0.58 (2012) to 0.73 (2025) — counterintuitively suggests
   INCREASING stickiness. But this reflects survivor bias: casual users leave, daily users remain.
   The denominator (MAU) growth slowed dramatically while DAU kept growing among the committed base.

2. **MAU growth deceleration**: ~45% YoY in 2012 → ~7% in 2017 → ~2% in 2022 → ~1% in 2024.
   Classic S-curve saturation consistent with maturation → senescence transition.

3. **Revenue-user divergence**: Revenue grew 56x (2012-2025) while MAU grew 3.5x.
   ARPU grew from $1.21 to $19.17 — the advertising ratchet extracting more value per user
   even as the platform senesces.

4. **Q4 seasonality**: Q4 revenue consistently spikes due to holiday advertising. ARPU
   in Q4 is always the yearly peak.
