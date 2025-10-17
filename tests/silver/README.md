# Silver Layer Tests

This directory contains tests for Silver layer data cleansing, validation, and transformation functionality.

## Test Scope

### Data Cleansing Tests
- Data standardization and normalization
- Duplicate detection and removal
- Data type conversion and casting
- Null value handling and imputation
- Format standardization validation

### Data Validation Tests
- Business rule compliance testing
- Schema validation and enforcement
- Data quality constraint verification
- Referential integrity checks
- Range and domain validation

### Transformation Tests
- Functional transformation pipeline testing
- Data enrichment and augmentation
- Derived column calculation validation
- Aggregation and grouping logic
- Performance optimization verification

## Test Structure

- `test_cleansing.py` - Data cleansing functionality tests
- `test_validation.py` - Data validation and quality tests
- `test_transformations.py` - Transformation pipeline tests
- `test_business_rules.py` - Business logic and rule tests
- `test_performance.py` - Performance and optimization tests
- `fixtures/` - Test data fixtures and expected results

## Usage

```bash
# Run all silver layer tests
pytest tests/silver/

# Run specific test files
pytest tests/silver/test_validation.py
pytest tests/silver/test_transformations.py

# Run with coverage
pytest --cov=src.silver tests/silver/
```

## Test Data

Silver layer tests use:
- Bronze layer output as input fixtures
- Business rule validation scenarios
- Data quality edge cases and anomalies
- Performance benchmarking datasets
- Expected transformation results