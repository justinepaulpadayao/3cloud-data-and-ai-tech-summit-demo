from pyspark.sql import SparkSession
from pyspark.sql.functions import col, expr

if __name__ == "__main__":
    accounts_df = spark.table("tech_summit_demo.silver.accounts")

    # 1. Credit Limit Utilization Ratio (No Built-in Functions)
    accounts_df = accounts_df.withColumn("credit_utilization_ratio",
                                          expr("current_balance / credit_limit"))

    # 2. Account Size Category (Based on Balance)
    accounts_df = accounts_df.withColumn("account_size_category",
                                          expr("CASE WHEN current_balance < 1000 THEN 'Small' "
                                               "WHEN current_balance >= 1000 AND current_balance < 10000 THEN 'Medium' "
                                               "ELSE 'Large' END"))

    # 3. Available Credit (Credit Limit - Current Balance)
    accounts_df = accounts_df.withColumn("available_credit",
                                          expr("credit_limit - current_balance"))

    # 4. Balance to Credit Limit Percentage
    accounts_df = accounts_df.withColumn("balance_to_limit_percentage",
                                          expr("(current_balance / credit_limit) * 100"))

    # 5. Risk Score (Based on Utilization and Balance)
    accounts_df = accounts_df.withColumn("risk_score",
                                          expr("CASE WHEN credit_utilization_ratio > 0.9 THEN 'High Risk' "
                                               "WHEN current_balance > 50000 THEN 'High Risk' "
                                               "ELSE 'Low Risk' END"))

    accounts_df.show()