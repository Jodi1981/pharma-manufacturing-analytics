# Data Loading

This step documents how manufacturing data was loaded into PostgreSQL.

## Source Data
The dataset represents simulated pharmaceutical manufacturing operations, including batches, products, equipment, and quality outcomes.

## Loading Method
Data was loaded using pgAdmin's Query Tool by executing a structured SQL script that:
- Created tables
- Applied primary and foreign keys
- Inserted records in dependency order

## Validation
After loading, basic validation queries were run to confirm:
- Row counts matched expectations
- Foreign key relationships were intact
- No NULLs existed in mandatory fields
