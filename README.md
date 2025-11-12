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

### 1. AI-Driven Development Structure

This project demonstrates how AI can enhance data engineering workflows through:

- **Memory Bank System**: Persistent project context tracking across sessions
  - `productContext.md` - Project overview and architecture
  - `activeContext.md` - Current work focus and recent changes
  - `progress.md` - Task tracking and completion status
  - `decisionLog.md` - Architectural decisions and rationale
  - `systemPatterns.md` - PySpark coding standards and patterns

- **Context7 Integration**: Up-to-date library documentation via MCP server
  - Real-time access to latest PySpark APIs
  - Version-specific documentation
  - Eliminates outdated code suggestions

- **Roocode Mode Collaboration**: Specialized AI modes for different tasks
  - 🏗️ **Architect Mode**: System design and architectural decisions
  - 💻 **Code Mode**: Feature implementation following standards
  - ❓ **Ask Mode**: Questions and documentation lookup
  - 🐛 **Debug Mode**: Error investigation and troubleshooting

### 2. PySpark Best Standards

All code strictly follows production-grade PySpark patterns defined in [`docs/standards/pyspark-coding-standards.md`](docs/standards/pyspark-coding-standards.md):

**Naming Conventions:**
- DataFrames: Suffix with `_df` (e.g., `customers_df`)
- Columns: PascalCase (e.g., `CustomerName`, `TotalBalance`)
- Functions: lower_snake_case with prefixes (`with_*`, `filter_*`, `remove_*`)

**Import Standards:**
```python
from pyspark.sql import functions as F
from pyspark.sql import types as T
from pyspark.sql import Window as W
```

**Functional Programming:**
- Extract complex logic into column functions
- Use transform functions for DataFrame operations
- Avoid UDFs - prefer native PySpark functions
- Maximum 79 characters per line
- Break before binary operators

**Example Transform Function:**
```python
def with_credit_utilization(df):
    """Add credit utilization ratio column.
    
    Args:
        df: DataFrame with CurrentBalance and CreditLimit columns
        
    Returns:
        DataFrame with CreditUtilizationRatio column
    """
    return df.withColumn(
        "CreditUtilizationRatio",
        F.when(F.col("CreditLimit") > 0,
               F.col("CurrentBalance") / F.col("CreditLimit"))
        .otherwise(0.0)
    )
```

### 3. Unit Testing Best Practices

Comprehensive testing strategy across all layers:

**Test Structure:**
- Unit tests for individual transformation functions
- Integration tests for layer-to-layer data flow
- Data quality validation tests
- Schema compliance tests

**Testing Pattern:**
```python
def test_with_credit_utilization(spark):
    """Test credit utilization calculation."""
    # Arrange
    data = [
        (1, 5000.0, 10000.0),
        (2, 8000.0, 10000.0),
        (3, 0.0, 10000.0)
    ]
    df = spark.createDataFrame(data, ["Id", "CurrentBalance", "CreditLimit"])
    
    # Act
    result_df = with_credit_utilization(df)
    
    # Assert
    assert result_df.filter(F.col("Id") == 1).select("CreditUtilizationRatio").collect()[0][0] == 0.5
    assert result_df.filter(F.col("Id") == 2).select("CreditUtilizationRatio").collect()[0][0] == 0.8
```

**Run Tests:**
```bash
pytest tests/ -v
```

See [`tests/README.md`](tests/README.md) for complete testing guidelines.

## 📚 Getting Started

### Quick Start

1. **Read the Documentation:**
   - [`docs/QUICK-START-CHECKLIST.md`](docs/QUICK-START-CHECKLIST.md) - Step-by-step setup guide (20 minutes)
   - [`docs/SETUP-GUIDE.md`](docs/SETUP-GUIDE.md) - Detailed configuration instructions

2. **Setup AI Development Environment:**
   - Install Roocode VS Code extension
   - Configure Context7 MCP for up-to-date documentation
   - Initialize Memory Bank system
   - Configure mode-specific instructions

3. **Install Dependencies:**
   ```bash
   # Prerequisites
   - Python 3.x
   - PySpark
   - Azure Blob Storage account
   - Databricks CLI (optional)
   - Node.js v18+ (for Context7)
   ```

4. **Databricks Connect:**
   - Virtual environment configured automatically by Databricks Connect
   - Follow: https://docs.databricks.com/gcp/en/dev-tools/databricks-connect/python

5. **Configuration:**
   - Create `config.yaml` in `configs/` directory
   - Configure Azure Blob Storage connection details
   - See [`configs/README.md`](configs/README.md) for details

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

### AI-Enhanced Development Workflow
1.  **Memory Bank Initialization**: Architect mode creates persistent project context
2.  **Context7 Integration**: Real-time access to latest PySpark documentation
3.  **Standards Enforcement**: systemPatterns.md ensures consistent code quality
4.  **Mode Collaboration**: Seamless handoffs between Architect, Code, Ask, and Debug modes
5.  **Automated Testing**: AI-recommended test coverage for all layers

### PySpark Engineering Excellence
1.  **Functional Programming**: Immutable transformations using `.transform()` methods
2.  **Column Functions**: Reusable, composable column expressions
3.  **Native Functions**: Zero UDFs - all transformations use PySpark native functions
4.  **Code Standards**: 79-character line limit, PascalCase columns, prefixed functions
5.  **Performance Optimization**: Efficient Spark operations with proper partitioning

### Testing & Quality Assurance
1.  **Comprehensive Coverage**: Unit and integration tests for all layers
2.  **Schema Validation**: Automated data contract enforcement
3.  **Data Quality Checks**: Built-in validation at each medallion layer
4.  **CI/CD Ready**: pytest integration for automated testing
5.  **AI-Driven Recommendations**: Intelligent test case suggestions

## License Information

This project is licensed under the [MIT License](LICENSE).

## Dependencies

*   PySpark
*   Other dependencies (specified in `requirements.txt`)

## Testing & Quality

### Running Tests

```bash
# Run all tests
pytest tests/ -v

# Run specific layer tests
pytest tests/bronze/ -v
pytest tests/silver/ -v
pytest tests/gold/ -v

# Run with coverage
pytest tests/ --cov=src --cov-report=html
```

### Testing Standards

- **Unit Tests**: Test individual transformation functions
- **Integration Tests**: Test layer-to-layer data flow
- **Schema Tests**: Validate data contracts
- **Quality Tests**: Data validation and completeness

See [`tests/README.md`](tests/README.md) for detailed testing guidelines.

## AI Development Workflow

### Daily Usage Pattern

1. **Morning**: Check Memory Bank status
   ```
   "What's the current focus?" (Ask mode)
   ```

2. **During Development**: Use appropriate modes
   - Design → Architect mode
   - Code → Code mode
   - Questions → Ask mode
   - Errors → Debug mode

3. **End of Day**: Sync Memory Bank
   ```
   "UMB" (Update Memory Bank)
   ```

### Context7 Usage

```python
# Automatic usage - just mention the library
"Implement PySpark window functions"
→ Automatically uses Context7 for latest PySpark docs

# Explicit usage
"use context7 for /apache/spark"
```

## Deployment

Deploy to production environment:

1.  Configure `config.yaml` with production settings
2.  Deploy PySpark scripts to Databricks cluster
3.  Schedule pipeline execution
4.  Monitor data quality metrics

See [`scripts/README.md`](scripts/README.md) for orchestration details.

## 📖 Documentation

- **Quick Start**: [`docs/QUICK-START-CHECKLIST.md`](docs/QUICK-START-CHECKLIST.md) ⭐ START HERE
- **Setup Guide**: [`docs/SETUP-GUIDE.md`](docs/SETUP-GUIDE.md)
- **PySpark Standards**: [`docs/standards/pyspark-coding-standards.md`](docs/standards/pyspark-coding-standards.md)
- **Roocode Configurations**: [`docs/roocode-mode-configurations/`](docs/roocode-mode-configurations/)