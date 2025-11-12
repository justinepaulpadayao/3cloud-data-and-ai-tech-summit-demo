# Silver Layer - Data Transformation

This directory contains code for the Silver layer of the medallion architecture, handling intermediate data transformations.

## Purpose

The Silver layer is responsible for:
- Cleansing and standardizing data from Bronze layer
- Applying business logic and rules
- Creating derived columns and calculations
- Implementing functional programming patterns
- Ensuring data quality and consistency

## Key Principles

- **Data Quality**: Cleanse and validate data
- **Business Logic**: Apply domain rules and transformations
- **Functional Programming**: Use composable, reusable functions
- **Type Conversions**: Standardize data types
- **Enrichment**: Add derived attributes

## Files

### [`account_silver.py`](account_silver.py:1)
Silver layer transformations for account data.

**Expected Functions:**
- Transform functions for account processing
- Business logic for credit calculations
- Data quality checks
- Derived column creation

## Data Flow

```
Bronze Layer → Silver Layer → Gold Layer
  (Raw Data)   (Cleansed)    (Analytics)
```

## Transformation Patterns

### Transform Functions
```python
from pyspark.sql import functions as F
from pyspark.sql import types as T

def with_credit_utilization(df):
    """Add credit utilization ratio column.
    
    Args:
        df: DataFrame with CurrentBalance and CreditLimit columns
        
    Returns:
        DataFrame with CreditUtilizationRatio column
    """
    return df.withColumn(
        "CreditUtilizationRatio",
        F.when(F.col("CreditLimit") > 0, 
               F.col("CurrentBalance") / F.col("CreditLimit"))
        .otherwise(0.0)
    )

def with_full_name(df):
    """Add full name from first and last names.
    
    Args:
        df: DataFrame with FirstName and LastName columns
        
    Returns:
        DataFrame with FullName column
    """
    return df.withColumn(
        "FullName",
        F.concat_ws(" ", F.col("FirstName"), F.col("LastName"))
    )
```

### Column Functions
```python
from pyspark.sql import functions as F

def is_high_risk(balance_col, limit_col):
    """Determine if account is high risk.
    
    Args:
        balance_col: Column name for current balance
        limit_col: Column name for credit limit
        
    Returns:
        Column expression for high risk flag
    """
    utilization = F.col(balance_col) / F.col(limit_col)
    return utilization > 0.8
```

## Composable Operations

Chain transformations using `.transform()`:

```python
from src.silver.account_transforms import (
    with_credit_utilization,
    with_risk_flag,
    with_standardized_status
)

result_df = (
    bronze_df
    .transform(with_credit_utilization)
    .transform(with_risk_flag)
    .transform(with_standardized_status)
)
```

## Common Transformations

### Data Cleansing
- Remove duplicates
- Handle null values
- Standardize formats
- Validate ranges

### Business Logic
- Calculate derived metrics
- Apply business rules
- Categorize data
- Create flags and indicators

### Type Conversions
- String to date conversions
- Numeric type standardization
- Boolean flag creation
- Enum mapping

## Usage Example

```python
from pyspark.sql import SparkSession
from pyspark.sql import functions as F

spark = SparkSession.builder.appName("Silver Layer").getOrCreate()

# Read from Bronze layer
accounts_bronze_df = spark.table("tech_summit_demo.bronze.accounts")

# Apply Silver transformations
accounts_silver_df = (
    accounts_bronze_df
    .withColumn(
        "CreditUtilizationRatio",
        F.when(F.col("CreditLimit") > 0,
               F.col("CurrentBalance") / F.col("CreditLimit"))
        .otherwise(0.0)
    )
    .withColumn(
        "IsHighRisk",
        F.col("CreditUtilizationRatio") > 0.8
    )
    .withColumn(
        "AccountStatus",
        F.upper(F.col("Status"))
    )
)

# Write to Silver table
accounts_silver_df.write.format("delta").mode("overwrite").saveAsTable(
    "tech_summit_demo.silver.accounts"
)
```

## Data Quality Checks

Implement validation functions:

```python
def validate_account_balance(df):
    """Validate account balances are non-negative.
    
    Args:
        df: DataFrame with CurrentBalance column
        
    Returns:
        DataFrame with invalid records filtered
    """
    return df.filter(F.col("CurrentBalance") >= 0)

def validate_credit_limit(df):
    """Validate credit limits are positive when present.
    
    Args:
        df: DataFrame with CreditLimit column
        
    Returns:
        DataFrame with valid credit limits
    """
    return df.filter(
        F.col("CreditLimit").isNull() | 
        (F.col("CreditLimit") > 0)
    )
```

## Integration Points

### Upstream
- **Bronze Layer**: Consumes raw data from [`src/bronze/`](../bronze/README.md)
- **Schema Definitions**: Uses schemas from [`src/schema/`](../schema/README.md)

### Downstream
- **Gold Layer**: Provides cleansed data to [`src/gold/`](../gold/README.md)
- **Testing**: Validated by tests in [`tests/`](../../tests/README.md)

## Coding Standards

Follows PySpark standards from [`docs/standards/pyspark-coding-standards.md`](../../docs/standards/pyspark-coding-standards.md):

### Key Conventions
- **Transform functions**: Prefix with `with_*`, `filter_*`, or `remove_*`
- **Column functions**: Return column expressions
- **Immutability**: Always return new DataFrame
- **Composability**: Design for chaining with `.transform()`

## Best Practices

- Extract complex logic into reusable functions
- Use `.select()` instead of multiple `.withColumn()` calls
- Avoid UDFs - prefer native PySpark functions
- Break before binary operators
- Maximum 79 characters per line
- Document function parameters and return types
- Write unit tests for transformation functions
- Use list comprehensions instead of loops
- Handle null values explicitly
- Log data quality metrics

## Performance Optimization

- Minimize shuffles by filtering early
- Cache intermediate results when reused
- Partition appropriately for downstream queries
- Use broadcast joins for small lookup tables
- Coalesce after filtering to reduce partitions