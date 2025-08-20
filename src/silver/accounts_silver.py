from pyspark.sql import SparkSession
from pyspark.sql.functions import col, to_date
from pyspark.sql.types import StructType, StructField, StringType, DoubleType

def process_accounts_data(spark):
    accounts_schema = StructType([
        StructField("account_id", StringType(), True),
        StructField("customer_id", StringType(), True),
        StructField("opening_date", StringType(), True),
        StructField("base_currency", StringType(), True),
        StructField("current_balance", DoubleType(), True),
        StructField("credit_limit", DoubleType(), True),
        StructField("status", StringType(), True)
    ])

    accounts_df = spark.table("tech_summit_demo.bronze.accounts")

    accounts_transformed = accounts_df.select(
        col("account_id"),
        col("customer_id"),
        col("opening_date"),
        col("base_currency"),
        col("current_balance"),
        col("credit_limit"),
        col("status")
    )

    accounts_transformed = accounts_transformed.withColumn("account_id", col("account_id").cast(StringType()))
    accounts_transformed = accounts_transformed.withColumn("customer_id", col("customer_id").cast(StringType()))
    accounts_transformed = accounts_transformed.withColumn("opening_date", to_date(col("opening_date"), "yyyy-MM-dd"))
    accounts_transformed = accounts_transformed.withColumn("base_currency", col("base_currency").cast(StringType()))
    accounts_transformed = accounts_transformed.withColumn("current_balance", col("current_balance").cast(DoubleType()))
    accounts_transformed = accounts_transformed.withColumn("credit_limit", col("credit_limit").cast(DoubleType()))
    accounts_transformed = accounts_transformed.withColumn("status", col("status").cast(StringType()))

    return accounts_transformed

if __name__ == "__main__":
    accounts_transformed = process_accounts_data(spark)
    accounts_transformed.show()