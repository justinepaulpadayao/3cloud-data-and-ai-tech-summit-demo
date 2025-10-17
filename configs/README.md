# Configuration Management

This directory contains configuration files and secrets management for the data engineering framework.

## Structure

- `development/` - Development environment configurations
- `staging/` - Staging environment configurations  
- `production/` - Production environment configurations
- `shared/` - Shared configuration templates and defaults

## Purpose

Centralized location for:
- Environment-specific configurations
- Database connection settings
- Spark cluster configurations
- Feature flags and runtime parameters
- Secret management templates

## Usage

Configuration files should follow the naming convention:
- `{service}_{environment}.yaml` for service-specific configs
- `global_{environment}.yaml` for environment-wide settings

## Security

Never commit actual secrets to version control. Use `.env` files and secret management tools for sensitive data.