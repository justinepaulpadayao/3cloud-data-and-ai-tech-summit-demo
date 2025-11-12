# 3Cloud GDC Data and AI Tech Summit Demo

## Project Overview

This project showcases the capabilities of **AI and Engineering Discipline in production-grade environment pipelines** for the **3Cloud GDC Data and AI Tech Summit**. It demonstrates an AI-driven, production-grade data engineering framework that leverages functional programming principles, Databricks Connect integration, and industry best practices.

The pipeline uses PySpark to ingest data from Azure Blob Storage, transform it through medallion architecture layers (Bronze → Silver → Gold), and demonstrates how AI can enhance data engineering workflows through intelligent recommendations, automated testing, and modular, composable utilities.

## Directory Structure

- **Configuration:** [`configs/`](configs/README.md) — Stores environment and connection settings.
- **Documentation:** [`docs/`](docs/README.md) — Project documentation.
- **Memory Bank:** [`memory-bank/`](memory-bank/productContext.md) — Tracks context, decisions, progress, and patterns.
- **Source Code:** [`src/`](src/bronze/README.md) — AI-enhanced pipeline code organized by medallion architecture:
  - [`bronze/`](src/bronze/README.md): Raw data ingestion with intelligent error handling.
  - [`silver/`](src/silver/README.md): Intermediate transformations using functional programming patterns.
  - [`gold/`](src/gold/README.md): Production-ready analytical datasets with AI-driven quality checks.
  - [`schema/`](src/schema/): Data validation schemas with automated inference capabilities.
- **Utilities:** [`utils/`](utils/README.md) — Modular, composable data processing and validation helpers.
- **Testing:** [`tests/`](tests/README.md) — AI-recommended unit/integration tests per layer.
- **Data:** [`data/`](data/README.md) — Sample financial datasets for summit demonstration.
- **Scripts:** [`scripts/`](scripts/README.md) — Production-grade pipeline orchestration scripts.

## Tech Summit Demo Features

### AI & Engineering Discipline Showcase

- **AI-Driven Data Quality**: Intelligent recommendations for test coverage and data validation
- **Functional Programming Paradigm**: Production-grade transformations using DataFrame `transform` methods
- **Memory Bank System**: Persistent project context for enhanced AI guidance and decision tracking
- **Modular Architecture**: Composable utilities demonstrating engineering best practices
- **Production-Grade Patterns**: Scalable, maintainable code adhering to industry standards

## Setup and Installation

1.  **Prerequisites:**
    *   Python 3.x
    *   PySpark
    *   Azure Blob Storage account
    *   Databricks CLI (if deploying to Databricks)

2.  **Databricks Connect Setup:**
    *   **Note:** The Python virtual environment will be configured automatically by Databricks Connect.
    *   Follow the official Databricks Connect setup guide for Python at: https://docs.databricks.com/gcp/en/dev-tools/databricks-connect/python to complete the environment setup process.

3.  **Configuration:**
    *   Create a `config.yaml` file in the `configs/` directory.
    *   Configure the Azure Blob Storage connection details, including the account name, container name, and paths to the data files.

## Demo Usage Examples

### AI-Enhanced Data Ingestion from Azure Blob Storage

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

### Production-Grade Functional Transformations

```python
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, expr

spark = SparkSession.builder.appName("Accounts Gold").getOrCreate()

accounts_df = spark.table("tech_summit_demo.silver.accounts")

accounts_df = accounts_df.withColumn("credit_utilization_ratio",
                                      expr("current_balance / credit_limit"))

accounts_df.show()
```

## Summit Demonstration Highlights

### AI Capabilities Demonstrated
1.  **Intelligent Data Quality**: AI-driven recommendations for comprehensive test coverage
2.  **Automated Pattern Recognition**: Smart identification of data transformation patterns
3.  **Context-Aware Processing**: Memory bank system maintains project intelligence across sessions
4.  **Predictive Analytics**: Forward-looking insights from processed financial datasets

### Engineering Discipline Excellence
1.  **Functional Programming**: Immutable transformations and composable operations
2.  **Production Standards**: Industry-grade error handling, logging, and monitoring
3.  **Modular Design**: Reusable, testable components following SOLID principles
4.  **Performance Optimization**: Efficient Spark operations with proper partitioning strategies

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