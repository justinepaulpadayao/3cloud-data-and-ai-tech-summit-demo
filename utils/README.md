# Utilities Directory

This directory contains modular, composable data processing and validation helpers.

## Purpose

Houses reusable utility functions for:
- Data validation and quality checks
- Common data transformations
- Error handling and logging
- File I/O operations
- Configuration management

## Key Principles

- **Modularity**: Single-purpose, focused utilities
- **Reusability**: Generic functions usable across layers
- **Composability**: Combine utilities for complex operations
- **Type Safety**: Strong typing with proper validation
- **Well-Tested**: Comprehensive unit test coverage

## Expected Utility Modules

### Data Validation (`validation.py`)
```python
from pyspark.sql import functions as F

def is_valid_email(col_name):
    """Validate email format.
    
    Args:
        col_name: Name of column containing email
        
    Returns:
        Column expression for email validation
    """
    email_pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return F.col(col_name).rlike(email_pattern)

def is_not_null_or_empty(col_name):
    """Check if column is not null or empty.
    
    Args:
        col_name: Name of column to check
        
    Returns:
        Column expression for non-null, non-empty validation
    """
    return (
        F.col(col_name).isNotNull() & 
        (F.trim(F.col(col_name)) != "")
    )
```

### Common Transformations (`transforms.py`)
```python
from pyspark.sql import functions as F

def standardize_phone_number(col_name):
    """Standardize phone number format.
    
    Args:
        col_name: Name of column containing phone number
        
    Returns:
        Column expression for standardized phone number
    """
    # Remove all non-numeric characters
    return F.regexp_replace(F.col(col_name), r"[^\d]", "")

def calculate_age_from_dob(dob_col_name, reference_date=None):
    """Calculate age from date of birth.
    
    Args:
        dob_col_name: Name of column containing date of birth
        reference_date: Reference date for calculation (default: current_date)
        
    Returns:
        Column expression for calculated age
    """
    ref_date = reference_date if reference_date else F.current_date()
    return F.floor(F.datediff(ref_date, F.col(dob_col_name)) / 365.25)
```

### Error Handling (`error_handling.py`)
```python
from pyspark.sql import functions as F

def with_error_flag(df, validation_expr, error_col_name="HasError"):
    """Add error flag column based on validation expression.
    
    Args:
        df: Input DataFrame
        validation_expr: Column expression for validation
        error_col_name: Name for error flag column
        
    Returns:
        DataFrame with error flag column
    """
    return df.withColumn(error_col_name, ~validation_expr)

def log_data_quality_metrics(df, table_name):
    """Log data quality metrics for DataFrame.
    
    Args:
        df: Input DataFrame
        table_name: Name of table for logging
        
    Returns:
        None (logs metrics)
    """
    total_rows = df.count()
    null_counts = {
        col: df.filter(F.col(col).isNull()).count()
        for col in df.columns
    }
    
    print(f"Table: {table_name}")
    print(f"Total Rows: {total_rows}")
    print(f"Null Counts: {null_counts}")
```

### Configuration Management (`config.py`)
```python
import os
from dotenv import load_dotenv

def load_config():
    """Load configuration from environment variables.
    
    Returns:
        Dictionary of configuration settings
    """
    load_dotenv()
    
    return {
        "azure_storage_account": os.getenv("AZURE_STORAGE_ACCOUNT"),
        "azure_container": os.getenv("AZURE_CONTAINER"),
        "azure_customer_path": os.getenv("AZURE_CUSTOMER_PATH"),
        "azure_account_path": os.getenv("AZURE_ACCOUNT_PATH"),
        "azure_transaction_path": os.getenv("AZURE_TRANSACTION_PATH")
    }

def get_azure_uri(container, storage_account, path):
    """Construct Azure Blob Storage URI.
    
    Args:
        container: Container name
        storage_account: Storage account name
        path: Path to data within container
        
    Returns:
        Formatted Azure URI string
    """
    return (
        f"abfss://{container}@{storage_account}"
        f".dfs.core.windows.net{path}"
    )
```

### File I/O (`io_utils.py`)
```python
from pyspark.sql import DataFrame

def read_parquet_safely(spark, path, schema=None):
    """Read parquet file with error handling.
    
    Args:
        spark: SparkSession
        path: Path to parquet file
        schema: Optional schema to enforce
        
    Returns:
        DataFrame or None if read fails
    """
    try:
        if schema:
            return spark.read.schema(schema).parquet(path)
        else:
            return spark.read.parquet(path)
    except Exception as e:
        print(f"Error reading parquet from {path}: {str(e)}")
        return None

def write_delta_table(df, table_name, mode="overwrite", partition_cols=None):
    """Write DataFrame to Delta table.
    
    Args:
        df: DataFrame to write
        table_name: Fully qualified table name
        mode: Write mode (overwrite, append, etc.)
        partition_cols: Optional list of partition columns
        
    Returns:
        None
    """
    writer = df.write.format("delta").mode(mode)
    
    if partition_cols:
        writer = writer.partitionBy(*partition_cols)
    
    writer.saveAsTable(table_name)
```

## Usage Across Layers

### Bronze Layer
```python
from utils.io_utils import read_parquet_safely
from utils.config import get_azure_uri, load_config

config = load_config()
uri = get_azure_uri(
    config["azure_container"],
    config["azure_storage_account"],
    config["azure_customer_path"]
)

customers_df = read_parquet_safely(spark, uri)
```

### Silver Layer
```python
from utils.validation import is_valid_email, is_not_null_or_empty
from utils.transforms import standardize_phone_number

silver_df = (
    bronze_df
    .filter(is_valid_email("Email"))
    .filter(is_not_null_or_empty("FirstName"))
    .withColumn("PhoneNumber", standardize_phone_number("PhoneNumber"))
)
```

### Gold Layer
```python
from utils.error_handling import log_data_quality_metrics

log_data_quality_metrics(gold_df, "customer_analytics")
```

## Integration Points

### Used By
- **Bronze Layer**: [`src/bronze/`](../src/bronze/README.md) - File I/O and config
- **Silver Layer**: [`src/silver/`](../src/silver/README.md) - Validation and transforms
- **Gold Layer**: [`src/gold/`](../src/gold/README.md) - Error handling and logging
- **Scripts**: [`scripts/`](../scripts/README.md) - Configuration and utilities

### Depends On
- **Configuration**: [`configs/`](../configs/README.md) - Environment settings
- **Schemas**: [`src/schema/`](../src/schema/README.md) - Type definitions

## Coding Standards

Follows PySpark standards from [`docs/standards/pyspark-coding-standards.md`](../docs/standards/pyspark-coding-standards.md):

```python
from pyspark.sql import functions as F

def with_audit_columns(df):
    """Add standard audit columns to DataFrame.
    
    Args:
        df: Input DataFrame
        
    Returns:
        DataFrame with audit columns added
    """
    return df.select(
        "*",
        F.current_timestamp().alias("CreatedTimestamp"),
        F.current_user().alias("CreatedBy")
    )
```

## Best Practices

- Keep utilities small and focused
- Write comprehensive docstrings
- Include type hints where possible
- Maintain backward compatibility
- Write unit tests for all utilities
- Avoid side effects in utility functions
- Use meaningful parameter names
- Handle errors gracefully
- Log important operations
- Document dependencies clearly

## Testing

All utilities should have corresponding tests in [`tests/utils/`](../tests/README.md):

```python
# tests/utils/test_validation.py
from utils.validation import is_valid_email
from pyspark.sql import functions as F

def test_is_valid_email(spark):
    data = [("user@example.com",), ("invalid-email",)]
    df = spark.createDataFrame(data, ["email"])
    
    result_df = df.filter(is_valid_email("email"))
    
    assert result_df.count() == 1
```

## Performance Considerations

- Prefer native PySpark functions over UDFs
- Cache reusable computations
- Minimize data shuffles
- Use broadcast for small lookup tables
- Profile utilities for bottlenecks