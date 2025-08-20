from pyspark.sql import SparkSession
from pyspark.sql.functions import col, to_date
from pyspark.sql.types import StructType, StructField, StringType

def process_customers_data(spark):
    customers_schema = StructType([
        StructField("customer_id", StringType(), True),
        StructField("name", StringType(), True),
        StructField("address", StringType(), True),
        StructField("tax_id", StringType(), True),
        StructField("incorporation_date", StringType(), True),
        StructField("country_code", StringType(), True),
        StructField("business_type", StringType(), True),
        StructField("risk_category", StringType(), True)
    ])

    customers_df = spark.table("tech_summit_demo.bronze.customers")

    customers_transformed = customers_df.select(
        col("customer_id"),
        col("name"),
        col("address"),
        col("tax_id"),
        col("incorporation_date"),
        col("country_code"),
        col("business_type"),
        col("risk_category")
    )

    customers_transformed = customers_transformed.withColumn("customer_id", col("customer_id").cast(StringType()))
    customers_transformed = customers_transformed.withColumn("name", col("name").cast(StringType()))
    customers_transformed = customers_transformed.withColumn("address", col("address").cast(StringType()))
    customers_transformed = customers_transformed.withColumn("tax_id", col("tax_id").cast(StringType()))
    customers_transformed = customers_transformed.withColumn("incorporation_date", to_date(col("incorporation_date"), "yyyy-MM-dd"))
    customers_transformed = customers_transformed.withColumn("country_code", col("country_code").cast(StringType()))
    customers_transformed = customers_transformed.withColumn("business_type", col("business_type").cast(StringType()))
    customers_transformed = customers_transformed.withColumn("risk_category", col("risk_category").cast(StringType()))

    return customers_transformed

if __name__ == "__main__":
    customers_transformed = process_customers_data(spark)
    customers_transformed.show()