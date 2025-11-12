# Bronze Layer - Raw Data Ingestion

This directory contains code for the Bronze layer of the medallion architecture, handling raw data ingestion from Azure Blob Storage.

## Purpose

The Bronze layer is responsible for:
- Ingesting raw data from source systems with minimal transformation
- Preserving data in its original format
- Applying basic schema validation
- Implementing intelligent error handling
- Logging data quality issues

## Key Principles

- **Raw Data Preservation**: Keep data as close to source format as possible
- **Schema Enforcement**: Apply predefined schemas for validation
- **Error Handling**: Gracefully handle malformed records
- **Auditability**: Track ingestion timestamps and source metadata
- **Idempotency**: Support reprocessing without duplicates

## Files

### [`files_to_bronze.py`](files_to_bronze.py:1)
Main ingestion script for loading data from Azure Blob Storage into Bronze tables.

**Functions:**
- Data reading from parquet files
- Schema validation against predefined schemas
- Error handling and logging
- Writing to Bronze Delta tables

## Data Flow

```
Azure Blob Storage → Bronze Layer → Delta Tables
    (Parquet)       (Validation)    (tech_summit_demo.bronze.*)
```

## Usage Example

```python
from pyspark.sql import SparkSession
import os
from dotenv import load_dotenv

load_dotenv()

spark = SparkSession.builder.appName("Bronze Ingestion").getOrCreate()

# Construct Azure Blob Storage URI
customer_uri = (
    f"abfss://{os.getenv('AZURE_CONTAINER')}"
    f"@{os.getenv('AZURE_STORAGE_ACCOUNT')}.dfs.core.windows.net"
    f"{os.getenv('AZURE_CUSTOMER_PATH')}"
)

# Read raw data
customers_df = spark.read.parquet(customer_uri)

# Write to Bronze table
customers_df.write.format("delta").mode("overwrite").saveAsTable(
    "tech_summit_demo.bronze.customers"
)
```

## Schema Validation

Bronze layer uses schemas from [`src/schema/`](../schema/README.md) to validate:
- Column names and data types
- Required fields presence
- Data format compliance

## Error Handling

Implements intelligent error handling:
- **Malformed Records**: Logged separately for investigation
- **Schema Mismatches**: Captured with detailed error messages
- **Missing Files**: Graceful failure with clear diagnostics
- **Partial Failures**: Continue processing valid records

## Integration Points

### Upstream
- **Azure Blob Storage**: Source data in Parquet format
- **Configuration**: Connection details from [`configs/`](../../configs/README.md)

### Downstream
- **Silver Layer**: Consumes Bronze tables from [`src/silver/`](../silver/README.md)
- **Testing**: Validated by tests in [`tests/`](../../tests/README.md)

## Coding Standards

Follows PySpark standards from [`docs/standards/pyspark-coding-standards.md`](../../docs/standards/pyspark-coding-standards.md):

```python
from pyspark.sql import functions as F
from pyspark.sql import types as T

def with_ingestion_timestamp(df):
    """Add ingestion timestamp to DataFrame.
    
    Args:
        df: Input DataFrame
        
    Returns:
        DataFrame with IngestionTimestamp column added
    """
    return df.withColumn("IngestionTimestamp", F.current_timestamp())
```

## Best Practices

- Use Delta format for ACID transactions
- Partition by date for efficient querying
- Implement incremental loading where possible
- Log all ingestion metrics
- Validate data quality at ingestion time
- Maintain schema versions for evolution tracking