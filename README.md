# Data Engineering Pipeline for Financial Data

## Project Overview

This project is a data engineering pipeline designed to process financial data. It uses PySpark to ingest data from Azure Blob Storage, transform it, and load it into a Delta Lake. The pipeline includes scripts for ingesting data from various sources and transforming it into a format suitable for analysis.

## Directory Structure

```
.
├── config/
│   └── config.yaml             # Configuration file
├── docs/
│   └── README.md             # Documentation
├── dummy-data/
│   ├── data_generators/        # Scripts for generating dummy data
│   └── data_validators/        # Scripts for validating dummy data
├── generated-data/           # Location for generated data
│   ├── account/                # Parquet files for account data
│   ├── customer/               # Parquet files for customer data
│   └── transaction/            # Parquet files for transaction data
├── memory-bank/              # Memory bank files
│   ├── activeContext.md        # Active context
│   ├── decisionLog.md          # Decision log
│   ├── productContext.md       # Product context
│   ├── progress.md             # Progress tracking
│   └── systemPatterns.md       # System patterns
├── src/
│   ├── bronze/                 # Bronze layer (raw data)
│   │   └── pyspark/            # PySpark scripts for bronze layer
│   ├── gold/                   # Gold layer (transformed data)
│   │   └── accounts_gold.py    # Script for transforming account data
│   ├── schema/                 # Schemas for data validation
│   └── silver/                 # Silver layer (intermediate data)
├── tests/
│   └── test_accounts_gold.py # Tests for accounts gold layer
├── typings/                  # Type definitions
└── utils/                    # Utility functions
```

## Setup and Installation

1.  **Prerequisites:**
    *   Python 3.x
    *   PySpark
    *   Azure Blob Storage account
    *   Databricks CLI (if deploying to Databricks)

2.  **Install Dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

    *(Note: The `requirements.txt` file is currently empty. Please add the required dependencies to this file.)*

3.  **Configuration:**
    *   Create a `config.yaml` file in the `config/` directory.
    *   Configure the Azure Blob Storage connection details, including the account name, container name, and paths to the data files.

## Usage Examples

### Ingesting Data from Azure Blob Storage

```python
from pyspark.sql import SparkSession
import os
from dotenv import load_dotenv

load_dotenv()

spark = SparkSession.builder.appName("Data Ingestion").getOrCreate()

customer_uri = f"abfss://{{os.getenv('AZURE_CONTAINER')}}@{{os.getenv('AZURE_STORAGE_ACCOUNT')}}.dfs.core.windows.net{{os.getenv('AZURE_CUSTOMER_PATH')}}"
customers_df = spark.read.parquet(customer_uri)
customers_df.show()
```

### Transforming Account Data

```python
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, expr

spark = SparkSession.builder.appName("Accounts Gold").getOrCreate()

accounts_df = spark.table("tech_summit_demo.silver.accounts")

accounts_df = accounts_df.withColumn("credit_utilization_ratio",
                                      expr("current_balance / credit_limit"))

accounts_df.show()
```

## Contribution Guidelines

1.  **Coding Style:** Follow the PEP 8 coding style for Python.
2.  **Branching Strategy:** Use feature branches for new features or bug fixes.
3.  **Pull Request Process:** Submit pull requests to the `main` branch.
4.  **Testing:** Write unit tests for all new code.
5.  **Bug Reports:** Report bugs by creating issues on the GitHub repository.
6.  **Feature Requests:** Suggest new features by creating issues on the GitHub repository.

## License Information

This project is licensed under the [MIT License](LICENSE).

## Dependencies

*   PySpark
*   Other dependencies (specified in `requirements.txt`)

## Testing

To run the tests, use the following command:

```bash
pytest tests/
```

## Deployment

To deploy the project to a production environment, follow these steps:

1.  Configure the `config.yaml` file with the production environment settings.
2.  Deploy the PySpark scripts to a Databricks cluster or other Spark environment.
3.  Schedule the scripts to run on a regular basis.