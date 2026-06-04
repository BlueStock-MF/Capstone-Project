# BlueStock Mutual Fund Analytics Project
# Data Dictionary

## Overview

This document describes all datasets used in the BlueStock Mutual Fund Analytics Project, including column definitions, data types, business meanings, and source references.

---

# 01_fund_master

**Source:** `data/raw/01_fund_master.csv`

| Column Name | Data Type | Business Definition |
|------------|-----------|--------------------|
| amfi_code | Integer | Unique AMFI scheme code assigned to each mutual fund scheme |
| scheme_name | Text | Name of the mutual fund scheme |
| fund_house | Text | Asset Management Company (AMC) managing the scheme |
| category | Text | Broad mutual fund category (Equity, Debt, etc.) |
| sub_category | Text | Detailed classification of the scheme |
| risk_category | Text | Risk level associated with the scheme |

---

# 02_nav_history

**Source:** `data/raw/02_nav_history.csv`

| Column Name | Data Type | Business Definition |
|------------|-----------|--------------------|
| amfi_code | Integer | AMFI scheme code |
| date | Date | NAV observation date |
| nav | Decimal | Net Asset Value per unit on the given date |

---

# 03_aum_by_fund_house

**Source:** `data/raw/03_aum_by_fund_house.csv`

| Column Name | Data Type | Business Definition |
|------------|-----------|--------------------|
| date | Date | Reporting date |
| fund_house | Text | Asset Management Company name |
| aum_lakh_crore | Decimal | Assets Under Management in lakh crore rupees |
| aum_crore | Decimal | Assets Under Management in crore rupees |
| num_schemes | Integer | Number of active schemes managed by the fund house |

---

# 04_monthly_sip_inflows

**Source:** `data/raw/04_monthly_sip_inflows.csv`

| Column Name | Data Type | Business Definition |
|------------|-----------|--------------------|
| month | Date | Reporting month |
| sip_inflow_crore | Decimal | Monthly SIP inflow amount in crore rupees |
| active_sip_accounts_crore | Decimal | Number of active SIP accounts (crores) |
| new_sip_accounts_lakh | Decimal | Number of newly registered SIP accounts (lakhs) |
| sip_aum_lakh_crore | Decimal | SIP assets under management in lakh crore rupees |
| yoy_growth_pct | Decimal | Year-over-year SIP growth percentage |

---

# 05_category_inflows

**Source:** `data/raw/05_category_inflows.csv`

| Column Name | Data Type | Business Definition |
|------------|-----------|--------------------|
| month | Date | Reporting month |
| category | Text | Mutual fund category |
| net_inflow_crore | Decimal | Net inflow or outflow amount in crore rupees |

---

# 06_industry_folio_count

**Source:** `data/raw/06_industry_folio_count.csv`

| Column Name | Data Type | Business Definition |
|------------|-----------|--------------------|
| month | Date | Reporting month |
| total_folios_crore | Decimal | Total mutual fund folios in crores |
| equity_folios_crore | Decimal | Equity mutual fund folios in crores |
| debt_folios_crore | Decimal | Debt mutual fund folios in crores |
| hybrid_folios_crore | Decimal | Hybrid mutual fund folios in crores |
| others_folios_crore | Decimal | Other category mutual fund folios in crores |

---

# 07_scheme_performance

**Source:** `data/raw/07_scheme_performance.csv`

| Column Name | Data Type | Business Definition |
|------------|-----------|--------------------|
| amfi_code | Integer | AMFI scheme code |
| scheme_name | Text | Name of the mutual fund scheme |
| fund_house | Text | Asset Management Company |
| category | Text | Mutual fund category |
| plan | Text | Direct or Regular plan |
| return_1yr_pct | Decimal | One-year annualized return (%) |
| return_3yr_pct | Decimal | Three-year annualized return (%) |
| return_5yr_pct | Decimal | Five-year annualized return (%) |
| benchmark_3yr_pct | Decimal | Benchmark three-year return (%) |
| alpha | Decimal | Risk-adjusted excess return measure |
| beta | Decimal | Volatility relative to benchmark |
| sharpe_ratio | Decimal | Risk-adjusted return indicator |
| sortino_ratio | Decimal | Downside-risk-adjusted return indicator |
| std_dev_ann_pct | Decimal | Annualized standard deviation (%) |
| max_drawdown_pct | Decimal | Maximum decline from peak (%) |
| aum_crore | Decimal | Assets Under Management in crore rupees |
| expense_ratio_pct | Decimal | Expense ratio (%) charged by the fund |
| morningstar_rating | Integer | Morningstar rating score |
| risk_grade | Text | Risk classification of the scheme |

---

# 08_investor_transactions

**Source:** `data/raw/08_investor_transactions.csv`

| Column Name | Data Type | Business Definition |
|------------|-----------|--------------------|
| investor_id | Text | Unique investor identifier |
| transaction_date | Date | Date of transaction |
| amfi_code | Integer | Mutual fund AMFI code |
| transaction_type | Text | Transaction type (SIP, Lumpsum, Redemption) |
| amount_inr | Decimal | Transaction amount in Indian Rupees |
| state | Text | Investor state |
| city | Text | Investor city |
| city_tier | Text | City classification (T30/B30) |
| age_group | Text | Investor age bracket |
| gender | Text | Investor gender |
| annual_income_lakh | Decimal | Annual income in lakh rupees |
| payment_mode | Text | Mode of payment used |
| kyc_status | Text | KYC verification status |

---

# 09_portfolio_holdings

**Source:** `data/raw/09_portfolio_holdings.csv`

| Column Name | Data Type | Business Definition |
|------------|-----------|--------------------|
| amfi_code | Integer | Mutual fund AMFI code |
| stock_symbol | Text | Stock ticker symbol |
| stock_name | Text | Name of the stock/security |
| sector | Text | Industry sector of the stock |
| weight_pct | Decimal | Portfolio allocation percentage |
| market_value_cr | Decimal | Market value of holding in crore rupees |
| current_price_inr | Decimal | Current market price of the stock |
| portfolio_date | Date | Portfolio disclosure date |

---

# 10_benchmark_indices

**Source:** `data/raw/10_benchmark_indices.csv`

| Column Name | Data Type | Business Definition |
|------------|-----------|--------------------|
| date | Date | Trading date |
| index_name | Text | Benchmark index name |
| close_value | Decimal | Closing value of benchmark index |

---

# Data Sources

| Dataset | Source |
|----------|---------|
| Fund Master | Internal Project Dataset |
| NAV History | Internal Project Dataset + MFAPI Validation |
| AUM Data | Internal Project Dataset |
| SIP Inflows | Internal Project Dataset |
| Category Inflows | Internal Project Dataset |
| Industry Folios | Internal Project Dataset |
| Scheme Performance | Internal Project Dataset |
| Investor Transactions | Internal Project Dataset |
| Portfolio Holdings | Internal Project Dataset |
| Benchmark Indices | Internal Project Dataset |

---

# Data Quality Notes

- Dates standardized using Pandas datetime conversion.
- Duplicate records removed where applicable.
- Missing NAV values forward-filled for holidays and weekends.
- Transaction amounts validated to be positive.
- Expense ratios validated within expected industry range.
- AMFI code consistency checked across datasets.
- Numeric columns validated and cleaned before database loading.
