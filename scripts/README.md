# Scripts Directory

This directory contains production-grade pipeline orchestration and deployment scripts.

## Purpose

Houses automation scripts for:
- Pipeline execution and orchestration
- Databricks job deployment
- Environment setup and configuration
- Batch processing workflows
- Data quality monitoring

## Expected Scripts

### Pipeline Orchestration
- **Main pipeline runners**: Execute end-to-end medallion architecture flows
- **Layer-specific runners**: Execute Bronze, Silver, or Gold layer independently
- **Incremental processing**: Handle delta loads and incremental updates

### Deployment Scripts
- **Databricks deployment**: Deploy notebooks and jobs to Databricks workspace
- **Configuration deployment**: Push environment-specific configurations
- **CI/CD integration**: Support automated deployment pipelines

### Utility Scripts
- **Data validation**: Pre-flight checks before pipeline execution
- **Monitoring**: Track pipeline performance and data quality metrics
- **Cleanup**: Archive or remove outdated data

## Usage Pattern

Scripts typically follow this pattern:

```bash
python scripts/run_bronze_layer.py --env production
python scripts/run_silver_layer.py --env production
python scripts/run_gold_layer.py --env production
```

Or orchestrate the full pipeline:

```bash
python scripts/run_full_pipeline.py --env production
```

## Configuration

Scripts read configuration from:
- [`configs/config.yaml`](../configs/README.md)
- Environment variables from `.env`
- Command-line arguments

## Integration with Source Code

Scripts orchestrate code from:
- [`src/bronze/`](../src/bronze/README.md) - Raw data ingestion
- [`src/silver/`](../src/silver/README.md) - Data transformation
- [`src/gold/`](../src/gold/README.md) - Analytical datasets

## Best Practices

- Use logging for observability
- Include error handling and retry logic
- Support dry-run mode for testing
- Document required permissions and dependencies
- Follow production deployment standards