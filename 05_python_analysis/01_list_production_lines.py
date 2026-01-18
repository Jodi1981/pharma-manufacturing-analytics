import psycopg2

# 1. Connect to PostgreSQL
conn = psycopg2.connect(
    host="localhost",
    port=5433,
    database="pharma_analytics",
    user="postgres",
    password="YOUR_Postgrsql_PASSWORD" 
)

# 2. Create cursor
cursor = conn.cursor()

# 3. SQL query (same logic we discussed)
query = """
SELECT DISTINCT production_line
FROM production_runs
ORDER BY production_line;
"""

# 4. Execute query
cursor.execute(query)

# 5. Fetch results
results = cursor.fetchall()

# 6. Print results cleanly
print("Production Lines:")
for row in results:
    print("-", row[0])

# 7. Close resources
cursor.close()
conn.close()
