Business Question:
Which production lines produced the highest total quantity?

SELECT
    production_line,
    SUM(quantity_produced) AS total_quantity_produced
FROM production_runs
GROUP BY production_line
ORDER BY total_quantity_produced DESC;
