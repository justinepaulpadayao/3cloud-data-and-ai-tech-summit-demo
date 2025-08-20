from pyspark.sql import SparkSession
from pyspark.sql.functions import col, expr

if __name__ == "__main__":
    customers_df = spark.table("tech_summit_demo.silver.customer")
    customers_df = customers_df.withColumn("customer_age_at_incorporation",
                                           expr("CAST(substring(incorporation_date, 1, 4) AS INT)"))

    customers_df = customers_df.withColumn("simplified_address",
                                           expr("substring(address, 1, 20)"))

    customers_df = customers_df.withColumn("has_tax_id",
                                           expr("CASE WHEN tax_id IS NOT NULL THEN 'Yes' ELSE 'No' END"))

    customers_df = customers_df.withColumn("business_type_length",
                                           expr("length(business_type)"))

    customers_df = customers_df.withColumn("country_code_group",
                                           expr("CASE WHEN country_code IN ('US', 'CA', 'GB') THEN 'North America/Europe' ELSE 'Other' END"))

    customers_df.show()
