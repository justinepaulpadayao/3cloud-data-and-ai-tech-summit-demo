# Source Code Directory

This directory contains the AI-enhanced pipeline code organized by medallion architecture layers.

## Purpose

Houses production-grade PySpark code implementing the medallion architecture pattern:
- **Bronze Layer**: Raw data ingestion with intelligent error handling
- **Silver Layer**: Intermediate transformations using functional programming patterns
- **Gold Layer**: Production-ready analytical datasets with AI-driven quality checks
- **Schema Layer**: Data validation schemas with automated inference capabilities

## Directory Structure

### [`bronze/`](bronze/README.md)
Raw data ingestion from Azure Blob Storage with:
- Minimal transformations
- Schema enforcement
- Error handling and logging
- Data quality checks

### [`silver/`](silver/README.md)
Intermediate data transformations with:
- Business logic application
- Data type conversions
- Derived columns and calculations
- Functional programming patterns

### [`gold/`](gold/README.md)
Production-ready analytical datasets with:
- Aggregations and analytics
- Denormalized views
- Performance optimization
- AI-driven quality validation

### [`schema/`](schema/README.md)
Data validation schemas with:
- PySpark StructType definitions
- Automated schema inference
- Schema evolution handling
- Data contract enforcement

## Coding Standards

All code follows the PySpark standards defined in [`docs/standards/pyspark-coding-standards.md`](../docs/standards/pyspark-coding-standards.md):

### Key Conventions
- **DataFrames**: Suffix with `_df` (e.g., `customers_df`)
- **Columns**: PascalCase naming
- **Functions**: lower_snake_case with prefixes (`with_*`, `filter_*`)
- **Imports**: Standard aliases (`F`, `T`, `W`)

### Example Pattern

```python
from pyspark.sql import functions as F
from pyspark.sql import types as T

def with_full_name(df):
    """Add FullName column from FirstName and LastName.
    
    Args:
        df: Input DataFrame with FirstName and LastName columns
        
    Returns:
        DataFrame with FullName column added
    """
    return df.withColumn(
        "FullName",
        F.concat_ws(" ", F.col("FirstName"), F.col("LastName"))
    )
```

## Functional Programming Approach

Code emphasizes:
- **Transform functions**: DataFrame operations as composable functions
- **Column functions**: Reusable column expressions
- **Immutability**: No in-place modifications
- **Composability**: Chain operations using `.transform()`

## Integration with Utilities

Source code leverages modular utilities from [`utils/`](../utils/README.md):
- Data validation helpers
- Common transformations
- Error handling utilities
- Logging and monitoring

## Testing

Corresponding tests are located in [`tests/`](../tests/README.md):
- Unit tests for individual functions
- Integration tests for layer pipelines
- Data quality validation tests

## Usage Example

```python
from pyspark.sql import SparkSession
from src.bronze.files_to_bronze import ingest_customers
from src.silver.account_silver import transform_accounts
from src.gold.customer_analytics import create_customer_gold

spark = SparkSession.builder.appName("Pipeline").getOrCreate()

# Bronze layer
bronze_df = ingest_customers(spark)

# Silver layer
silver_df = transform_accounts(bronze_df)

# Gold layer
gold_df = create_customer_gold(silver_df)