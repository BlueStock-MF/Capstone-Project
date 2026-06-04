-- 1. Top 5 Funds by AUM

SELECT
    scheme_name,
    aum_crore
FROM scheme_performance
ORDER BY aum_crore DESC
LIMIT 5;


-- 2. Average NAV Per Month

SELECT
    substr(date,1,7) AS month,
    ROUND(AVG(nav),2) AS avg_nav
FROM nav_history
GROUP BY month
ORDER BY month;


-- 3. SIP YoY Growth

SELECT
    substr(month,1,4) AS year,
    AVG(yoy_growth_pct) AS avg_yoy_growth
FROM monthly_sip_inflows
GROUP BY year;


-- 4. Transactions By State

SELECT
    state,
    COUNT(*) AS total_transactions
FROM investor_transactions
GROUP BY state
ORDER BY total_transactions DESC;


-- 5. Funds With Expense Ratio Below 1%

SELECT
    scheme_name,
    expense_ratio_pct
FROM scheme_performance
WHERE expense_ratio_pct < 1
ORDER BY expense_ratio_pct;


-- 6. Top 10 Funds By 5-Year Return

SELECT
    scheme_name,
    return_5yr_pct
FROM scheme_performance
ORDER BY return_5yr_pct DESC
LIMIT 10;


-- 7. Average Return By Category

SELECT
    category,
    ROUND(AVG(return_3yr_pct),2) AS avg_return
FROM scheme_performance
GROUP BY category;


-- 8. KYC Status Distribution

SELECT
    kyc_status,
    COUNT(*) AS investors
FROM investor_transactions
GROUP BY kyc_status;


-- 9. Top Cities By Investment Amount

SELECT
    city,
    ROUND(SUM(amount_inr),2) AS total_investment
FROM investor_transactions
GROUP BY city
ORDER BY total_investment DESC
LIMIT 10;


-- 10. Fund Houses By AUM

SELECT
    fund_house,
    ROUND(SUM(aum_crore),2) AS total_aum
FROM aum_by_fund_house
GROUP BY fund_house
ORDER BY total_aum DESC;