# Configuration Directory

This directory contains configuration files for the Tech Summit Demo project.

## Purpose

Stores environment-specific settings and connection configurations for:
- Azure Blob Storage credentials
- Databricks connection details
- Environment variables
- Pipeline parameters

## Required Configuration

### `config.yaml`

Create a `config.yaml` file in this directory with the following structure:

```yaml
azure:
  storage_account: "<your-storage-account-name>"
  container: "<your-container-name>"
  customer_path: "/path/to/customer/data"
  account_path: "/path/to/account/data"
  transaction_path: "/path/to/transaction/data"

databricks:
  catalog: "tech_summit_demo"
  schema_bronze: "bronze"
  schema_silver: "silver"
  schema_gold: "gold"
```

## Environment Variables

Alternatively, use a `.env` file in the project root with:

```
AZURE_STORAGE_ACCOUNT=<your-storage-account>
AZURE_CONTAINER=<your-container>
AZURE_CUSTOMER_PATH=/path/to/customer/data
AZURE_ACCOUNT_PATH=/path/to/account/data
AZURE_TRANSACTION_PATH=/path/to/transaction/data
```

## Security Notes

- Never commit sensitive credentials to version control
- Use `.gitignore` to exclude `config.yaml` and `.env` files
- Consider using Azure Key Vault for production deployments