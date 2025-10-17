# Data Validation Utilities

This module contains utilities for data quality testing and validation operations.

## Purpose

Functional utilities for:
- Data quality checks and assertions
- Schema validation and enforcement
- Completeness and consistency testing
- Anomaly detection and outlier identification
- Data profiling and statistics
- Custom validation rules and constraints

## Design Patterns

- **Composable Validators**: Chain multiple validation functions together
- **Pure Functions**: All validators return validation results without side effects
- **Functional Approach**: Use higher-order functions for validation composition
- **Type Safety**: Comprehensive type hints for validation functions

## Key Modules

- `quality_checks.py` - Core data quality validation functions
- `schema_validators.py` - Schema validation and enforcement utilities
- `completeness.py` - Data completeness and null value checks
- `consistency.py` - Data consistency and referential integrity checks
- `anomaly_detection.py` - Statistical anomaly and outlier detection
- `custom_rules.py` - Framework for custom validation rules

## Usage Example

```python
from utils.validation.quality_checks import validate_not_null, validate_range
from utils.validation.completeness import check_completeness

validation_results = df.transform(validate_not_null('customer_id')) \
                      .transform(validate_range('amount', min_val=0)) \
                      .transform(check_completeness)
```

## Contributing

- Follow functional programming principles
- Return structured validation results
- Include comprehensive test coverage
- Document validation logic and thresholds