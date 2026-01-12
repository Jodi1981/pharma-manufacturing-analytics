Business Question:
What is the average quantity produced per run for each production line?
This helps identify efficiency differences between lines.

SELECT
    production_line,
    AVG(quantity_produced) AS avg_quantity_per_run
FROM production_runs
GROUP BY production_line
ORDER BY avg_quantity_per_run DESC;
