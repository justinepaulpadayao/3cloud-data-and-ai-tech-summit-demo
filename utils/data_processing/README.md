# Data Processing Utilities

This module contains utilities for data transformation and processing operations.

## Purpose

Functional utilities for:
- Data transformations and aggregations
- Column operations and manipulations
- DataFrame reshaping and restructuring
- Data type conversions and casting
- Window functions and analytics
- Join operations and data merging

## Design Patterns

- **Pure Functions**: All transformations are implemented as pure functions
- **DataFrame Transform**: Utilize the DataFrame `transform` method for chaining
- **Composability**: Functions designed to be easily composed together
- **Type Safety**: Comprehensive type hints for all function signatures

## Key Modules

- `transformations.py` - Core data transformation functions
- `aggregations.py` - Aggregation and grouping utilities
- `joins.py` - Join operation helpers and patterns
- `window_functions.py` - Window function utilities
- `type_conversions.py` - Data type conversion helpers

## Usage Example

```python
from utils.data_processing.transformations import clean_column_names
from utils.data_processing.aggregations import calculate_metrics

df.transform(clean_column_names) \
  .transform(calculate_metrics)
```

## Contributing

- Follow functional programming principles
- Include comprehensive docstrings and type hints
- Add unit tests for all new functions
- Ensure functions are composable and chainable