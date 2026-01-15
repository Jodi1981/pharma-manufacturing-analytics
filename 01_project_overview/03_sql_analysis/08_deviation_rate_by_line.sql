KPI: Deviation Rate by Production Line
Definition:
Percentage of production runs that have at least one recorded deviation.
Formula:
(Deviation Runs / Total Runs) * 100




SELECT
pr.production_line,
COUNT(DISTINCT pr.run_id) AS total_runs,
COUNT(DISTINCT d.run_id) AS deviation_runs,
ROUND(
(COUNT(DISTINCT d.run_id)::numeric 
/ COUNT(DISTINCT pr.run_id)) * 100,
2
) AS deviation_rate_percent
FROM production_runs pr
LEFT JOIN deviations d
ON pr.run_id = d.run_id
GROUP BY pr.production_line
ORDER BY deviation_rate_percent DESC;
