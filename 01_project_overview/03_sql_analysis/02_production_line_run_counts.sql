-- Production line run counts
-- Purpose: Identify which production lines execute the most production runs

SELECT
    production_line,
    COUNT(*) AS total_runs
FROM production_runs
GROUP BY production_line
ORDER BY total_runs DESC;
