import os
from dotenv import load_dotenv
from pyspark.sql import SparkSession

load_dotenv()
required_vars = ['AZURE_STORAGE_ACCOUNT', 'AZURE_CONTAINER',
                'AZURE_CUSTOMER_PATH', 'AZURE_TRANSACTION_PATH',
                'AZURE_ACCOUNT_PATH', 'CATALOG_NAME']

missing = [var for var in required_vars if not os.getenv(var)]
if missing:
    raise ValueError(f"Missing env vars: {', '.join(missing)}")

# 3. Build URIs
customer_uri = f"abfss://{os.getenv('AZURE_CONTAINER')}@{os.getenv('AZURE_STORAGE_ACCOUNT')}.dfs.core.windows.net{os.getenv('AZURE_CUSTOMER_PATH')}"
transaction_uri = f"abfss://{os.getenv('AZURE_CONTAINER')}@{os.getenv('AZURE_STORAGE_ACCOUNT')}.dfs.core.windows.net{os.getenv('AZURE_TRANSACTION_PATH')}"
account_uri = f"abfss://{os.getenv('AZURE_CONTAINER')}@{os.getenv('AZURE_STORAGE_ACCOUNT')}.dfs.core.windows.net{os.getenv('AZURE_ACCOUNT_PATH')}"

# 4. Load datasets
loaded_dfs = {}
successful = 0

# Customer data
customers_df = spark.read.parquet(customer_uri)
if customers_df.count() == 0:
    pass
elif 'customer_id' not in customers_df.columns:
    pass
else:
    loaded_dfs['customers'] = customers_df
    successful += 1

# Transaction data
transactions_df = spark.read.parquet(transaction_uri)
if transactions_df.count() == 0:
    pass
elif 'transaction_id' not in transactions_df.columns:
    pass
else:
    loaded_dfs['transactions'] = transactions_df
    successful += 1

# Account data
accounts_df = spark.read.parquet(account_uri)
if accounts_df.count() == 0:
    pass
elif 'account_id' not in accounts_df.columns:
    pass
else:
    loaded_dfs['accounts'] = accounts_df
    successful += 1

# 5. Final validation
if successful == 0:
    raise SystemExit(1)

# Write datasets to Delta Lake bronze layer
catalog_name = os.getenv('CATALOG_NAME')
for table_name, df in loaded_dfs.items():
    df.write.format("delta") \
        .mode("overwrite") \
        .saveAsTable(f"{catalog_name}.bronze.{table_name}")