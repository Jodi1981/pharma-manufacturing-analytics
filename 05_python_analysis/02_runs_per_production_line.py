import psycopg2

# 1. Connect to PostgreSQL
conn = psycopg2.connect(
    host="localhost",
    port=5433,
    database="pharma_analytics",
    user="postgres",
    password="YOUR_POSTGRESQL_PASSWORD"
)

# 2. Create cursor
cursor = conn.cursor()

# 3. SQL query for KPI
query = """
SELECT
    production_line,
    COUNT(*) AS total_runs
FROM production_runs
GROUP BY production_line
ORDER BY total_runs DESC;
"""

# 4. Execute query
cursor.execute(query)

# 5. Fetch results
results = cursor.fetchall()

# 6. Print KPI output
print("Production Runs per Production Line")
print("----------------------------------")

for row in results:
    production_line = row[0]
    total_runs = row[1]
    print(f"{production_line} : {total_runs}")

# 7. Close resources
cursor.close()
conn.close()
