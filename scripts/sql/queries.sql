-- 1. Top 5 funds by AUM
SELECT fund_house, MAX(aum_crore)
FROM 03_aum_by_fund_house_clean
GROUP BY fund_house
ORDER BY MAX(aum_crore) DESC
LIMIT 5;

-- 2. Average NAV by scheme
SELECT amfi_code, AVG(nav)
FROM 02_nav_history_clean
GROUP BY amfi_code;

-- 3. Transactions by state
SELECT state, COUNT(*) AS txn_count
FROM 08_investor_transactions_clean
GROUP BY state
ORDER BY txn_count DESC;

-- 4. Expense ratio < 1%
SELECT scheme_name, expense_ratio_pct
FROM 07_scheme_performance_clean
WHERE expense_ratio_pct < 1;

-- 5. Average return by category
SELECT category, AVG(return_3yr_pct)
FROM 07_scheme_performance_clean
GROUP BY category;

-- 6. Total investment amount
SELECT SUM(amount_inr)
FROM 08_investor_transactions_clean;

-- 7. Count funds by fund house
SELECT fund_house, COUNT(*)
FROM 01_fund_master_clean
GROUP BY fund_house;

-- 8. Highest NAV
SELECT MAX(nav)
FROM 02_nav_history_clean;

-- 9. Portfolio sector allocation
SELECT sector, SUM(weight_pct)
FROM 09_portfolio_holdings_clean
GROUP BY sector;

-- 10. Benchmark average close value
SELECT index_name, AVG(close_value)
FROM 10_benchmark_indices_clean
GROUP BY index_name;