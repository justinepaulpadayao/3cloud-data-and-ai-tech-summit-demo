# Data Directory

This directory contains sample financial datasets used for the Tech Summit Demo.

## Purpose

Stores demonstration data files showcasing:
- Customer information
- Account details
- Transaction records
- Sample datasets for pipeline testing

## Expected Data Structure

### Customer Data
- **Format**: Parquet
- **Contains**: Customer demographics, contact information, account relationships

### Account Data
- **Format**: Parquet
- **Contains**: Account details, balances, credit limits, account types

### Transaction Data
- **Format**: Parquet
- **Contains**: Transaction history, amounts, timestamps, transaction types

## Data Source

Data is typically ingested from Azure Blob Storage. Local files in this directory are for:
- Development testing
- Demo purposes
- Pipeline validation

## Usage

Pipeline scripts in [`src/bronze/`](../src/bronze/README.md) read data from either:
1. Azure Blob Storage (production)
2. Local data directory (development/testing)

## Data Privacy

- All sample data is synthetic and generated for demonstration purposes
- No real customer information is stored
- Follow data governance policies when adding new datasets