# Bronze Layer Tests

This directory contains tests for Bronze layer ingestion and raw data processing functionality.

## Test Scope

### Ingestion Tests
- Source system connectivity validation
- Data extraction accuracy and completeness
- Schema inference and handling
- Error handling for malformed data
- Retry logic and resilience testing

### Raw Data Processing Tests
- Minimal transformation validation
- Metadata enrichment verification
- Audit trail and lineage tracking
- Data type preservation testing
- Volume and performance testing

### Data Quality Tests
- Source data validation rules
- Completeness and consistency checks
- Duplicate detection testing
- Schema evolution handling
- Data freshness validation

## Test Structure

- `test_ingestion.py` - Data ingestion functionality tests
- `test_raw_processing.py` - Raw data processing tests
- `test_quality_checks.py` - Bronze layer data quality tests
- `test_error_handling.py` - Error handling and resilience tests
- `fixtures/` - Test data fixtures and mock objects

## Usage

```bash
# Run all bronze layer tests
pytest tests/bronze/

# Run specific test files
pytest tests/bronze/test_ingestion.py
pytest tests/bronze/test_quality_checks.py

# Run with verbose output
pytest -v tests/bronze/
```

## Test Data

Bronze layer tests use:
- Mock source system data
- Simulated API responses
- Sample files in various formats (CSV, JSON, Parquet)
- Error scenarios and edge cases
- Performance test datasets