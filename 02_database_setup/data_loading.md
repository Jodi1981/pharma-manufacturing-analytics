# Data Loading (PostgreSQL)

Due to limitations encountered when restoring a large SQL dump via pgAdmin,
the dataset was loaded using the PostgreSQL command-line interface (`psql`).

This approach is commonly used in production environments for reliability
and better error visibility.

## Command Used

```cmd
psql ^
  -h localhost ^
  -p 5433 ^
  -U postgres ^
  -d pharma_analytics ^
  -f "C:\pg_backup\pharma_manufacturing_verified.sql"

## Validation

After the restore completed successfully, basic validation was performed
to confirm that data was loaded correctly.

The following query was used to validate row counts in the core table:

```sql
SELECT COUNT(*) 
FROM production_runs;

This confirmed that the expected volume of data (100,000 records) was successfully loaded.

Additional validation included:

Spot-checking sample records for expected values

Verifying no restore errors were reported by psql
