# SQL Analysis

This folder contains all SQL queries used during the analysis phase of the project.

Each SQL file represents a specific business question or analysis step.
Queries are written incrementally to reflect real-world exploration and problem solving.

The focus is on:
- Understanding manufacturing performance
- Identifying trends and inefficiencies
- Supporting operational and quality-related insights

## Execution Evidence (pgAdmin)

The following screenshots provide visual confirmation that the SQL queries
in this folder were executed against the PostgreSQL database using pgAdmin.

These screenshots demonstrate:
- Successful query execution
- Real data returned from the `production_runs` table
- Validation of analytical results used in later stages

Key KPIs Covered

The SQL analyses in this folder support the following manufacturing KPIs:

- Production run volume and validation
- Output distribution by production line
- Average run duration by production line
- Average output per run
- Throughput efficiency (units produced per hour)

Each KPI is implemented as a standalone SQL script to allow
independent execution, testing, and reuse.



