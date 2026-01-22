Python KPI #2
Deviation rate per production line


import psycopg2

# 1. Connect to PostgreSQL
conn = psycopg2.connect(
    host="localhost",
    port=5433,
    database="pharma_analytics",
    user="postgres",
    password="YOUR_PASSWORD"
)

# 2. Create cursor
cursor = conn.cursor()

# 3. SQL query for deviation rate KPI
query = """
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
"""

# 4. Execute query
cursor.execute(query)

# 5. Fetch results
results = cursor.fetchall()

# 6. Print KPI output
print("Deviation Rate per Production Line")
print("---------------------------------")

for row in results:
    production_line = row[0]
    total_runs = row[1]
    deviation_runs = row[2]
    deviation_rate = row[3]

    print(
        f"{production_line} | "
        f"Total Runs: {total_runs} | "
        f"Deviation Runs: {deviation_runs} | "
        f"Deviation Rate: {deviation_rate}%"
    )

# 7. Close resources
cursor.close()
conn.close()
