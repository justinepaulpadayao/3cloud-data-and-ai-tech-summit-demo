# Gold Layer - Production-Ready Analytics

This directory contains code for the Gold layer of the medallion architecture, creating production-ready analytical datasets.

## Purpose

The Gold layer is responsible for:
- Creating business-ready analytical datasets
- Implementing aggregations and complex analytics
- Building denormalized views for reporting
- Optimizing query performance
- Applying AI-driven quality validation

## Key Principles

- **Business-Centric**: Data organized for business consumption
- **Performance Optimized**: Pre-aggregated for fast queries
- **Denormalized**: Simplified structures for analytics
- **Quality Assured**: AI-driven validation and testing
- **Well-Documented**: Clear metadata and lineage

## Expected Files

### Analytics Modules
- **Customer Analytics**: Customer lifetime value, segmentation, behavior analysis
- **Account Analytics**: Account performance, risk metrics, portfolio analysis
- **Transaction Analytics**: Transaction patterns, trends, anomaly detection

### Common Patterns

```python
from pyspark.sql import functions as F
from pyspark.sql import types as T
from pyspark.sql import Window as W

def create_customer_analytics(df):
    """Create customer analytics gold table.
    
    Args:
        df: Silver layer customer DataFrame
        
    Returns:
        Gold layer customer analytics DataFrame
    """
    return df.select(
        F.col("CustomerId"),
        F.col("FullName"),
        F.count("AccountId").alias("TotalAccounts"),
        F.sum("CurrentBalance").alias("TotalBalance"),
        F.avg("CreditUtilizationRatio").alias("AvgUtilization")
    ).groupBy("CustomerId", "FullName")
```

## Data Flow

```
Silver Layer → Gold Layer → Analytics/BI Tools
  (Cleaned)   (Aggregated)   (Dashboards/Reports)
```

## Aggregation Types

### Customer-Level Aggregations
- Total accounts per customer
- Lifetime value calculations
- Credit utilization metrics
- Transaction summaries

### Account-Level Aggregations
- Account performance metrics
- Risk scoring
- Balance trends
- Activity patterns

### Time-Based Aggregations
- Monthly/quarterly summaries
- Trend analysis
- Seasonal patterns
- Year-over-year comparisons

## Usage Example

```python
from pyspark.sql import SparkSession
from pyspark.sql import functions as F

spark = SparkSession.builder.appName("Gold Layer").getOrCreate()

# Read from Silver layer
accounts_silver_df = spark.table("tech_summit_demo.silver.accounts")
customers_silver_df = spark.table("tech_summit_demo.silver.customers")

# Create Gold analytics
customer_analytics_df = (
    accounts_silver_df
    .join(customers_silver_df, "CustomerId")
    .groupBy("CustomerId", "FullName")
    .agg(
        F.count("AccountId").alias("TotalAccounts"),
        F.sum("CurrentBalance").alias("TotalBalance"),
        F.avg(F.col("CurrentBalance") / F.col("CreditLimit")).alias("AvgUtilization")
    )
)

# Write to Gold table
customer_analytics_df.write.format("delta").mode("overwrite").saveAsTable(
    "tech_summit_demo.gold.customer_analytics"
)
```

## Performance Optimization

- **Partitioning**: By date or key business dimensions
- **Z-Ordering**: On frequently filtered columns
- **Caching**: For frequently accessed datasets
- **Pre-Aggregation**: Compute heavy metrics once
- **Materialized Views**: For complex joins

## AI-Driven Quality Checks

Implements intelligent validation:
- **Metric Thresholds**: AI-recommended acceptable ranges
- **Anomaly Detection**: Identify unusual patterns
- **Completeness Checks**: Ensure comprehensive coverage
- **Consistency Validation**: Cross-table relationship verification

## Integration Points

### Upstream
- **Silver Layer**: Consumes cleaned data from [`src/silver/`](../silver/README.md)
- **Schema Definitions**: Uses schemas from [`src/schema/`](../schema/README.md)

### Downstream
- **BI Tools**: Power BI, Tableau, Looker
- **Data Science**: ML model training datasets
- **Reporting**: Executive dashboards and KPIs

## Coding Standards

Follows PySpark standards from [`docs/standards/pyspark-coding-standards.md`](../../docs/standards/pyspark-coding-standards.md):

```python
from pyspark.sql import functions as F
from pyspark.sql import Window as W

def with_customer_rank(df):
    """Add customer ranking by total balance.
    
    Args:
        df: Customer analytics DataFrame
        
    Returns:
        DataFrame with CustomerRank column
    """
    window_spec = W.orderBy(F.col("TotalBalance").desc())
    return df.withColumn("CustomerRank", F.row_number().over(window_spec))
```

## Best Practices

- Design for end-user consumption
- Optimize for common query patterns
- Document business logic clearly
- Maintain historical snapshots
- Implement slowly changing dimensions where appropriate
- Validate data quality before publishing
- Monitor query performance regularly