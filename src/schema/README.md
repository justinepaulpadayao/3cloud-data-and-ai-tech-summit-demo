# Schema Directory

This directory contains data validation schemas with automated inference capabilities.

## Purpose

Houses PySpark schema definitions for:
- Data type validation across all layers
- Schema enforcement during ingestion
- Automated schema inference from source data
- Schema evolution tracking
- Data contract enforcement

## Key Principles

- **Type Safety**: Explicit data type definitions
- **Validation**: Enforce data contracts
- **Documentation**: Clear field descriptions
- **Evolution**: Support schema changes over time
- **Reusability**: Share schemas across layers

## Expected Schema Files

### Customer Schema
```python
from pyspark.sql import types as T

customer_schema = T.StructType([
    T.StructField("CustomerId", T.StringType(), False),
    T.StructField("FirstName", T.StringType(), False),
    T.StructField("LastName", T.StringType(), False),
    T.StructField("Email", T.StringType(), True),
    T.StructField("PhoneNumber", T.StringType(), True),
    T.StructField("DateOfBirth", T.DateType(), True),
    T.StructField("CreatedDate", T.TimestampType(), False)
])
```

### Account Schema
```python
from pyspark.sql import types as T

account_schema = T.StructType([
    T.StructField("AccountId", T.StringType(), False),
    T.StructField("CustomerId", T.StringType(), False),
    T.StructField("AccountType", T.StringType(), False),
    T.StructField("CurrentBalance", T.DecimalType(18, 2), False),
    T.StructField("CreditLimit", T.DecimalType(18, 2), True),
    T.StructField("OpenedDate", T.DateType(), False),
    T.StructField("Status", T.StringType(), False)
])
```

### Transaction Schema
```python
from pyspark.sql import types as T

transaction_schema = T.StructType([
    T.StructField("TransactionId", T.StringType(), False),
    T.StructField("AccountId", T.StringType(), False),
    T.StructField("TransactionDate", T.TimestampType(), False),
    T.StructField("Amount", T.DecimalType(18, 2), False),
    T.StructField("TransactionType", T.StringType(), False),
    T.StructField("Description", T.StringType(), True)
])
```

## Schema Inference

Automated schema inference utilities:

```python
from pyspark.sql import functions as F

def infer_schema_from_sample(df, sample_size=1000):
    """Infer schema from sample data.
    
    Args:
        df: Input DataFrame
        sample_size: Number of rows to sample
        
    Returns:
        Inferred StructType schema
    """
    sample_df = df.limit(sample_size)
    return sample_df.schema

def validate_schema_compatibility(source_schema, target_schema):
    """Validate if source schema is compatible with target.
    
    Args:
        source_schema: Source StructType schema
        target_schema: Target StructType schema
        
    Returns:
        Boolean indicating compatibility
    """
    # Implementation for schema compatibility checks
    pass
```

## Usage in Pipeline

### Bronze Layer
```python
from src.schema.customer_schema import customer_schema

# Apply schema during read
customers_df = spark.read.schema(customer_schema).parquet(source_path)
```

### Schema Validation
```python
from src.schema.validation import validate_dataframe_schema

# Validate DataFrame against schema
is_valid = validate_dataframe_schema(df, customer_schema)
if not is_valid:
    raise ValueError("Schema validation failed")
```

## Schema Evolution

Handle schema changes gracefully:

```python
def merge_schemas(old_schema, new_schema):
    """Merge old and new schemas for evolution.
    
    Args:
        old_schema: Existing StructType schema
        new_schema: New StructType schema
        
    Returns:
        Merged StructType schema
    """
    # Add new fields from new_schema
    # Preserve existing fields from old_schema
    # Handle type changes carefully
    pass
```

## Integration Points

### Upstream
- **Source Systems**: Define expected data contracts
- **Configuration**: Schema versioning metadata

### Downstream
- **Bronze Layer**: Schema enforcement at ingestion in [`src/bronze/`](../bronze/README.md)
- **Silver Layer**: Type conversions in [`src/silver/`](../silver/README.md)
- **Gold Layer**: Analytics schema in [`src/gold/`](../gold/README.md)

## Coding Standards

Follows PySpark standards from [`docs/standards/pyspark-coding-standards.md`](../../docs/standards/pyspark-coding-standards.md):

```python
from pyspark.sql import types as T

def create_schema(fields):
    """Create StructType schema from field definitions.
    
    Args:
        fields: List of tuples (name, type, nullable)
        
    Returns:
        StructType schema
    """
    return T.StructType([
        T.StructField(name, dtype, nullable)
        for name, dtype, nullable in fields
    ])
```

## Best Practices

- Define schemas explicitly for all data sources
- Document field meanings and constraints
- Version schemas when making changes
- Test schema compatibility before deployment
- Use nullable fields judiciously
- Prefer specific types over generic ones (e.g., DecimalType over DoubleType for currency)
- Maintain schema registry for tracking
- Implement schema validation in CI/CD pipelines

## Schema Versioning

Maintain version history:

```python
# customer_schema_v1.py - Initial version
# customer_schema_v2.py - Added Email field
# customer_schema_v3.py - Made PhoneNumber nullable

# Current version
from src.schema.customer_schema_v3 import customer_schema