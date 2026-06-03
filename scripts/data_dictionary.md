# Data Dictionary

## 01_fund_master

| Column | Type | Description |
|----------|---------|------------|
| amfi_code | Integer | Unique AMFI scheme identifier |
| fund_house | String | Mutual fund company |
| scheme_name | String | Mutual fund scheme name |
| category | String | Fund category |
| sub_category | String | Fund sub-category |
| plan | String | Direct/Regular plan |
| launch_date | Date | Scheme launch date |
| benchmark | String | Benchmark index |
| expense_ratio_pct | Float | Expense ratio percentage |
| exit_load_pct | Float | Exit load percentage |
| min_sip_amount | Integer | Minimum SIP amount |
| min_lumpsum_amount | Integer | Minimum lumpsum amount |
| fund_manager | String | Fund manager name |
| risk_category | String | Risk classification |
| sebi_category_code | String | SEBI category code |

## 02_nav_history

| Column | Type | Description |
|----------|---------|------------|
| amfi_code | Integer | Scheme identifier |
| date | Date | NAV date |
| nav | Float | Net Asset Value |