# Gold Layer Tests

This directory contains tests for Gold layer business aggregations, analytics, and reporting functionality.

## Test Scope

### Business Aggregation Tests
- Time-series aggregation validation
- Customer and product analytics testing
- KPI and metrics calculation verification
- Cross-dimensional analysis testing
- Performance optimization validation

### Analytics Tests
- Business intelligence query testing
- Dashboard data preparation validation
- Report generation accuracy testing
- Data mart consistency verification
- Self-service analytics validation

### Performance Tests
- Query performance benchmarking
- Large dataset aggregation testing
- Concurrent user load testing
- Memory and resource utilization
- Caching and optimization validation

## Test Structure

- `test_aggregations.py` - Business aggregation functionality tests
- `test_metrics.py` - KPI and metrics calculation tests
- `test_analytics.py` - Analytics and business intelligence tests
- `test_data_marts.py` - Data mart and dimensional model tests
- `test_performance.py` - Performance and scalability tests
- `test_reports.py` - Report generation and validation tests
- `fixtures/` - Test data fixtures and expected business results

## Usage

```bash
# Run all gold layer tests
pytest tests/gold/

# Run specific test files
pytest tests/gold/test_aggregations.py
pytest tests/gold/test_metrics.py

# Run performance tests
pytest tests/gold/test_performance.py -m performance
```

## Test Data

Gold layer tests use:
- Silver layer output as input fixtures
- Business scenario test cases
- Historical data for trend analysis
- Performance benchmarking datasets
- Expected business metric results

## Business Validation

Tests include validation of:
- Financial calculations and accounting rules
- Customer segmentation and analytics
- Product performance metrics
- Operational KPIs and dashboards
- Regulatory and compliance reporting