KPI: Average production run duration per production line
Purpose:
Measures average runtime (in seconds) for each production line.
Used to identify bottlenecks and performance differences across lines.

SELECT
    production_line,
    EXTRACT(EPOCH FROM (AVG(end_time - start_time))) AS avg_run_duration_seconds
FROM production_runs
GROUP BY production_line
ORDER BY avg_run_duration_seconds DESC;
