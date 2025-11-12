import os

from databricks.connect import DatabricksSession

# Load environment variables
ABFSS_BASE_URL = os.getenv("ABFSS_BASE_URL")
AZURE_ACCOUNT_PATH = os.getenv("AZURE_ACCOUNT_PATH")
AZURE_CUSTOMER_PATH = os.getenv("AZURE_CUSTOMER_PATH")
AZURE_TRANSACTION_PATH = os.getenv("AZURE_TRANSACTION_PATH")

spark = DatabricksSession.builder.getOrCreate()

# Read account data using environment variables
account_path = f"{ABFSS_BASE_URL}{AZURE_ACCOUNT_PATH}"
customer_path = f"{ABFSS_BASE_URL}{AZURE_CUSTOMER_PATH}"
transaction_path = f"{ABFSS_BASE_URL}{AZURE_TRANSACTION_PATH}"

# Debug prints to verify paths
print(f"Account path: {account_path}")
print(f"Customer path: {customer_path}")
print(f"Transaction path: {transaction_path}")

# Show account data
df = spark.read.parquet(account_path)
df.show()
