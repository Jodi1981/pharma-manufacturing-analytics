Throughput KPI: Units produced per hour by production line

SELECT
    production_line,
    ROUND(
        SUM(quantity_produced) /
        NULLIF(
            SUM(EXTRACT(EPOCH FROM (end_time - start_time))) / 3600,
            0
        ),
        2
    ) AS units_per_hour
FROM production_runs
GROUP BY production_line
ORDER BY units_per_hour DESC;
