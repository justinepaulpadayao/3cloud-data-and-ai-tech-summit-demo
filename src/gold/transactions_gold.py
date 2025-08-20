from pyspark.sql import SparkSession
from pyspark.sql.functions import col, expr

if __name__ == "__main__":
    spark = SparkSession.builder.appName("TransactionsGold").getOrCreate()

    transactions_df = spark.table("tech_summit_demo.silver.transaction")

    transactions_df = transactions_df.withColumn("absolute_amount",
                                                   expr("abs(amount)"))

    transactions_df = transactions_df.withColumn("amount_category",
                                                   expr("CASE WHEN amount < 0 THEN 'Debit' ELSE 'Credit' END"))

    transactions_df = transactions_df.withColumn("simplified_description",
                                                   expr("substring(description, 1, 15)"))

    transactions_df = transactions_df.withColumn("converted_amount_difference",
                                                   expr("amount - converted_amount"))

    transactions_df = transactions_df.withColumn("high_value_transaction",
                                                   expr("CASE WHEN amount > 1000 THEN 'Yes' ELSE 'No' END"))

    transactions_df.show()

    spark.stop()