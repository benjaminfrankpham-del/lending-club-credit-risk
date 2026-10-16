
SELECT COUNT(*) AS loans,
       ROUND(AVG(is_default) * 100, 2) AS default_rate_pct
FROM loans