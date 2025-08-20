from pyspark.sql import SparkSession
from pyspark.sql.functions import col, to_date
from pyspark.sql.types import StructType, StructField, StringType, DoubleType

def process_transactions_data(spark):
    transactions_schema = StructType([
        StructField("transaction_id", StringType(), True),
        StructField("account_id", StringType(), True),
        StructField("timestamp", StringType(), True),
        StructField("amount", DoubleType(), True),
        StructField("counterparty", StringType(), True),
        StructField("transaction_type", StringType(), True),
        StructField("description", StringType(), True),
        StructField("converted_amount", DoubleType(), True),
        StructField("exchange_rate", DoubleType(), True)
    ])

    transactions_df = spark.table("tech_summit_demo.bronze.transactions")

    transactions_transformed = transactions_df.select(
        col("transaction_id"),
        col("account_id"),
        col("timestamp"),
        col("amount"),
        col("counterparty"),
        col("transaction_type"),
        col("description"),
        col("converted_amount"),
        col("exchange_rate")
    )

    transactions_transformed = transactions_transformed.withColumn("transaction_id", col("transaction_id").cast(StringType()))
    transactions_transformed = transactions_transformed.withColumn("account_id", col("account_id").cast(StringType()))
    transactions_transformed = transactions_transformed.withColumn("timestamp", to_date(col("timestamp"), "yyyy-MM-dd HH:mm:ss"))
    transactions_transformed = transactions_transformed.withColumn("amount", col("amount").cast(DoubleType()))
    transactions_transformed = transactions_transformed.withColumn("counterparty", col("counterparty").cast(StringType()))
    transactions_transformed = transactions_transformed.withColumn("transaction_type", col("transaction_type").cast(StringType()))
    transactions_transformed = transactions_transformed.withColumn("description", col("description").cast(StringType()))
    transactions_transformed = transactions_transformed.withColumn("converted_amount", col("converted_amount").cast(DoubleType()))
    transactions_transformed = transactions_transformed.withColumn("exchange_rate", col("exchange_rate").cast(DoubleType()))

    return transactions_transformed

if __name__ == "__main__":
    transactions_transformed = process_transactions_data(spark)
    transactions_transformed.show()