# [Project Name] - Data Engineering Platform

## Project Overview

[Brief description of what this data engineering project aims to accomplish. What business problems are you solving with data?]

Example: Building a modern data platform to enable data-driven decision making through automated ETL pipelines, robust data quality frameworks, and self-service analytics capabilities.

---

## Business Context

### Problem Statement
[What business challenge or opportunity is driving this project?]

### Expected Business Impact
- [Impact 1: e.g., Reduce manual reporting time by X%]
- [Impact 2: e.g., Enable real-time visibility into key metrics]
- [Impact 3: e.g., Improve data accuracy and reliability]

---

## Project Goals

### Primary Objectives
- [ ] [Goal 1: e.g., Build automated data pipelines for key business processes]
- [ ] [Goal 2: e.g., Establish data quality monitoring and alerting]
- [ ] [Goal 3: e.g., Create unified data models for reporting]
- [ ] [Goal 4: e.g., Enable self-service analytics for stakeholders]

### Success Metrics
- [Metric 1: e.g., Pipeline reliability > 99.5%]
- [Metric 2: e.g., Data freshness < 24 hours]
- [Metric 3: e.g., User adoption of dashboards]
- [Metric 4: e.g., Reduction in data-related support tickets]

---

## Technical Stack

### Cloud Platform
- **Provider**: Microsoft Azure
- **Primary Services**: [List Azure services being used]

### Data Processing
- **Framework**: PySpark
- **Platform**: [Choose one or specify]
  - Microsoft Fabric (Spark, Data Engineering workloads)
  - Azure Databricks (if using)
  - _Note: Pipelines designed to be portable between platforms_
- **Language**: Python 3.9+
- **Notebooks**: [Fabric Notebooks / Databricks Notebooks]

### Data Storage
- **Data Lake**: Azure Data Lake Storage Gen2 (ADLS)
- **Data Warehouse**: [Specify: Fabric Data Warehouse / Azure Synapse / etc.]
- **Architecture Pattern**: Medallion (Bronze → Silver → Gold)

### Business Intelligence
- **Primary BI Tool**: Microsoft PowerBI
- **Report Distribution**: PowerBI Service
- **Data Models**: [Semantic Models / Power BI Datasets]

### Data Sources & APIs
- **Planning System**: Anaplan (via API)
  - [Specify: Models/modules being integrated]
  - [API version/endpoints used]
- **Additional Sources**: [List other data sources]
  - [ERP systems]
  - [CRM systems]
  - [Other APIs]

### Development Tools
- **IDE**: VS Code with extensions
  - Roocode (AI-assisted development)
  - Python extensions
  - Fabric/Databricks extensions (as applicable)
- **Version Control**: Git / Azure DevOps Repos
- **Package Management**: pip, requirements.txt
- **Testing**: pytest, data quality frameworks

### Orchestration & Automation
- **Workflow**: [Specify: Fabric Pipelines / Azure Data Factory / Databricks Workflows]
- **Scheduling**: [Fabric Scheduler / ADF Triggers / Databricks Jobs]
- **Monitoring**: [Azure Monitor / Fabric Monitoring]

---

## Data Architecture

### Layered Architecture (Medallion)

```
Bronze Layer (Raw)
    ↓
    Extract data as-is from sources
    Minimal transformation
    Full historical data
    
Silver Layer (Cleaned)
    ↓
    Cleansed and validated
    Standardized schemas
    Business logic applied
    
Gold Layer (Curated)
    ↓
    Business-ready datasets
    Aggregated metrics
    Optimized for reporting
```

### Key Data Domains
- [Domain 1: e.g., Finance & Planning (from Anaplan)]
- [Domain 2: e.g., Operations]
- [Domain 3: e.g., Sales & Marketing]
- [Domain 4: Add as needed]

### Data Quality Framework
- **Validation Rules**: [Great Expectations / Custom PySpark checks]
- **Monitoring**: Automated data quality dashboards
- **Alerting**: [Specify alerting mechanism]
- **Standards**: Based on defined data quality dimensions

---

## Integration Points

### Anaplan Integration
- **Type**: REST API
- **Authentication**: [Basic / OAuth / Certificate]
- **Data Flow**: 
  - [Direction: Anaplan → Data Lake]
  - [Direction: Data Lake → Anaplan (if applicable)]
- **Key Models/Modules**: [List specific Anaplan models]
- **Sync Frequency**: [Daily / Hourly / Real-time]

### PowerBI Integration
- **Connection Type**: [DirectQuery / Import / Composite]
- **Data Sources**: Gold layer datasets
- **Refresh Schedule**: [Specify refresh cadence]
- **Key Reports/Dashboards**: [List main reporting outputs]

### Additional Integrations
- [System 1]: [Connection details]
- [System 2]: [Connection details]

---

## Development Standards

### Code Quality
- PySpark coding standards strictly enforced
- Documented in: `docs/standards/pyspark-coding-standards.md`
- Key principles:
  - Use F, T, W imports for PySpark
  - DataFrame suffix: `_df`
  - Column names: PascalCase
  - Functions: lower_snake_case with prefixes (with_*, filter_*, etc.)
  - No UDFs unless absolutely necessary
  - Maximum 79 characters per line

### Documentation
- All pipelines documented with purpose, inputs, outputs
- Data lineage tracked
- Decision log maintained in Memory Bank

### Testing
- Unit tests for all column functions
- Integration tests for pipelines
- Data quality tests on outputs
- Minimum 80% code coverage (where applicable)

---

## Project Phases

### Phase 1: Foundation
- [ ] Environment setup (Fabric/Databricks workspace)
- [ ] Bronze layer ingestion from key sources
- [ ] Base data quality framework
- [ ] Initial PowerBI connection

### Phase 2: Core Pipelines
- [ ] Silver layer transformations
- [ ] Gold layer business logic
- [ ] Anaplan API integration
- [ ] Automated orchestration

### Phase 3: Analytics & Reporting
- [ ] PowerBI semantic models
- [ ] Key business dashboards
- [ ] Self-service data access
- [ ] User training and documentation

### Phase 4: Optimization & Scale
- [ ] Performance tuning
- [ ] Advanced data quality monitoring
- [ ] Enhanced automation
- [ ] Expand to additional data sources

---

## Key Stakeholders

### Business Stakeholders
- [Name/Role]: [Responsibility/Interest]
- [Name/Role]: [Responsibility/Interest]

### Technical Team
- Data Engineering: [Team members/roles]
- BI/Analytics: [Team members/roles]
- Platform/DevOps: [Team members/roles]

### End Users
- [Department 1]: [Use cases]
- [Department 2]: [Use cases]

---

## Constraints & Considerations

### Technical Constraints
- [Constraint 1: e.g., Must work within Azure tenant security policies]
- [Constraint 2: e.g., Limited to Fabric free/Pro capacity]
- [Constraint 3: e.g., Anaplan API rate limits]

### Business Constraints
- [Constraint 1: e.g., Timeline requirements]
- [Constraint 2: e.g., Budget limitations]
- [Constraint 3: e.g., Resource availability]

### Data Governance
- Data classification requirements
- Compliance requirements (GDPR, SOC2, etc.)
- Access control policies
- Retention policies

---

## Risks & Mitigations

| Risk | Impact | Likelihood | Mitigation |
|------|--------|------------|------------|
| [e.g., Anaplan API changes] | High | Medium | [Version pinning, monitoring, fallback options] |
| [e.g., Data quality issues] | High | Medium | [Automated validation, alerts, remediation procedures] |
| [e.g., Platform limitations] | Medium | Low | [Design for portability, monitor limits] |

---

## Success Criteria

### Technical Success
- ✅ All pipelines running with >99% reliability
- ✅ Data quality checks passing consistently
- ✅ End-to-end data latency meets SLA
- ✅ Code quality standards maintained
- ✅ Full test coverage achieved

### Business Success
- ✅ Stakeholders using dashboards regularly
- ✅ Data-driven decisions being made
- ✅ Reduction in manual data work
- ✅ Improved data accuracy and trust
- ✅ Positive user feedback

---

## Additional Notes

### Platform Flexibility
This project is designed to leverage either Microsoft Fabric or Azure Databricks for PySpark workloads. The medallion architecture and PySpark code patterns remain consistent across platforms, with only minor adjustments needed for platform-specific features.

### Scalability Considerations
- Bronze layer: Scalable storage in ADLS
- Silver layer: Optimized partitioning strategies
- Gold layer: Pre-aggregated for performance
- PowerBI: Incremental refresh where appropriate

### Future Enhancements
- [Enhancement 1: e.g., Real-time streaming pipelines]
- [Enhancement 2: e.g., Machine learning integration]
- [Enhancement 3: e.g., Advanced analytics capabilities]
- [Enhancement 4: e.g., Data catalog implementation]

---

## Quick Reference

**Platform**: Microsoft Azure (Fabric/Databricks)  
**Primary Language**: Python (PySpark)  
**BI Tool**: PowerBI  
**Key Integration**: Anaplan API  
**Architecture**: Medallion (Bronze/Silver/Gold)  
**Development**: VS Code + Roocode + Memory Bank

---

**Last Updated**: [Date]  
**Project Status**: [Planning / In Progress / Production]  
**Next Review**: [Date]