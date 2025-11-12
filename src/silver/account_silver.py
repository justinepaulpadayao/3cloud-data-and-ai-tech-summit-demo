import os
from databricks.connect import DatabricksSession
from pyspark.sql import functions as F
from pyspark.sql.types import DecimalType

# TODO: Standardize this transformation later - currently adhoc implementation
# TODO: Move to Azure Key Vault for secure credential management

# Load environment variables
ABFSS_BASE_URL = os.getenv("ABFSS_BASE_URL")
AZURE_ACCOUNT_PATH = os.getenv("AZURE_ACCOUNT_PATH")
CATALOG_NAME = os.getenv("CATALOG_NAME", "tech_summit_demo")

spark = DatabricksSession.builder.getOrCreate()

# Read bronze account data
account_path = f"{ABFSS_BASE_URL}{AZURE_ACCOUNT_PATH}"
print(f"Reading from: {account_path}")

df_bronze = spark.read.parquet(account_path)

# Adhoc Silver Transformations
# 1. Convert opening_date from string to proper timestamp
# 2. Add derived columns for analysis
# 3. Clean status field (trim and standardize)
# 4. Calculate credit utilization
# 5. Add processing metadata

df_silver = df_bronze \
    .withColumn("opening_date_ts", F.to_timestamp("opening_date")) \
    .withColumn("status_clean", F.trim(F.upper(F.col("status")))) \
    .withColumn("current_balance_decimal", F.col("current_balance").cast(DecimalType(18, 2))) \
    .withColumn("credit_limit_decimal", F.col("credit_limit").cast(DecimalType(18, 2))) \
    .withColumn("credit_utilization_pct",
                F.when(F.col("credit_limit") > 0,
                       (F.col("current_balance") / F.col("credit_limit")) * 100)
                .otherwise(0)) \
    .withColumn("is_active", F.when(F.col("status_clean") == "ACTIVE", True).otherwise(False)) \
    .withColumn("is_closed", F.when(F.col("status_clean") == "CLOSED", True).otherwise(False)) \
    .withColumn("is_dormant", F.when(F.col("status_clean") == "DORMANT", True).otherwise(False)) \
    .withColumn("account_age_days", F.datediff(F.current_date(), F.col("opening_date_ts"))) \
    .withColumn("processed_at", F.current_timestamp()) \
    .withColumn("processing_date", F.current_date())

# Select final columns
df_final = df_silver.select(
    "account_id",
    "customer_id",
    "opening_date_ts",
    "base_currency",
    "current_balance_decimal",
    "credit_limit_decimal",
    "credit_utilization_pct",
    "status_clean",
    "is_active",
    "is_closed",
    "is_dormant",
    "account_age_days",
    "processed_at",
    "processing_date"
)

# Show sample results
print("\n=== Silver Account Data Sample ===")
df_final.show(10, truncate=False)

# Show some quick stats
print("\n=== Account Status Summary ===")
df_final.groupBy("status_clean").count().show()

print("\n=== Average Credit Utilization by Status ===")
df_final.groupBy("status_clean") \
    .agg(
        F.avg("credit_utilization_pct").alias("avg_credit_utilization"),
        F.avg("account_age_days").alias("avg_account_age_days"),
        F.count("*").alias("account_count")
    ).show()

print("\n=== Transformation Complete ===")
print(f"Total records processed: {df_final.count()}")
