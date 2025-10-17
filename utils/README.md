# Utilities

This directory contains modular utility functions organized by functional area.

## Structure

- `data_processing/` - Data transformation and processing utilities
- `validation/` - Data quality and validation utilities
- `common/` - Shared utility functions and helpers
- `spark/` - Spark-specific utilities and extensions

## Design Principles

- **Functional Programming**: All utilities follow functional programming paradigms
- **Composability**: Functions are designed to be easily composed and chained
- **Type Safety**: Proper type hints and validation for all functions
- **Testability**: Each utility is independently testable
- **Reusability**: Common patterns extracted into reusable components

## Usage Patterns

- Use DataFrame `transform` method for chaining operations
- Follow single-responsibility principle
- Implement pure functions where possible
- Use descriptive function names and comprehensive docstrings

## Contributing

When adding new utilities:
1. Place them in the appropriate functional subdirectory
2. Include comprehensive type hints and docstrings
3. Add corresponding unit tests
4. Follow the established functional programming patterns
5. Update relevant documentation