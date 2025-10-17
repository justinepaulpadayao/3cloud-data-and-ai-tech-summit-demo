# Data Engineering Pipeline for Financial Data

## Project Overview

This project is a data engineering pipeline designed to process financial data. It uses PySpark to ingest data from Azure Blob Storage, transform it, and load it into a Delta Lake. The pipeline includes scripts for ingesting data from various sources and transforming it into a format suitable for analysis.

## Directory Structure

- **Configuration:** [`configs/`](configs/README.md) — Stores environment and connection settings.
- **Documentation:** [`docs/`](docs/README.md) — Project documentation.
- **Memory Bank:** [`memory-bank/`](memory-bank/productContext.md) — Tracks context, decisions, progress, and patterns.
- **Source Code:** [`src/`](src/bronze/README.md) — Pipeline code by layer:
  - [`bronze/`](src/bronze/README.md): Raw data ingestion.
  - [`silver/`](src/silver/README.md): Intermediate transformations.
  - [`gold/`](src/gold/README.md): Final transformations.
  - [`schema/`](src/schema/): Data validation schemas.
- **Utilities:** [`utils/`](utils/README.md) — Data processing and validation helpers.
- **Testing:** [`tests/`](tests/README.md) — Unit/integration tests per layer.
- **Data:** [`data/`](data/README.md) — Input/output data files.
- **Scripts:** [`scripts/`](scripts/README.md) — Standalone pipeline scripts.

## Setup and Installation

1.  **Prerequisites:**
    *   Python 3.x
    *   PySpark
    *   Azure Blob Storage account
    *   Databricks CLI (if deploying to Databricks)

2.  **Databricks Connect Setup:**
    *   **Note:** The Python virtual environment will be configured automatically by Databricks Connect.
    *   Follow the official Databricks Connect setup guide for Python at: https://docs.databricks.com/gcp/en/dev-tools/databricks-connect/python to complete the environment setup process.

3.  **Install Dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

    *(Note: The `requirements.txt` file is currently empty. Please add the required dependencies to this file.)*

4.  **Configuration:**
    *   Create a `config.yaml` file in the `configs/` directory.
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