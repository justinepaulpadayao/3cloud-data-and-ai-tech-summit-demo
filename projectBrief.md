# Project Brief: AI-Driven Data Engineering Framework

## Purpose

This project establishes a comprehensive boilerplate, framework, and guide for leveraging AI within a modern data engineering workflow. It is designed to maximize the value of the project brief and memory bank, ensuring that architectural decisions and implementation strategies are informed by both human and AI-driven insights.

## Memory Bank Integration

The memory bank serves as a persistent context repository, capturing project goals, architectural decisions, progress, and recurring patterns. It enables AI agents to maintain continuity, reference historical context, and make recommendations that align with the evolving needs of the project.

## Functional Programming Principles & Production-Grade Practices

Functional programming is central to this framework, especially for developing robust, maintainable, and scalable data quality tests and utilities. The codebase adheres to industry best practices, including:

- **Immutability:** Data structures are not mutated, ensuring predictable behavior.
- **Pure Functions:** All transformations and utilities are implemented as pure functions, facilitating testability and reliability.
- **Composability:** Functions are designed to be modular and composable, enabling chaining and reuse.
- **Single-Responsibility Principle:** Each transformation function performs only one distinct operation, promoting clarity and maintainability.
- **Type Safety:** Where possible, type hints and static analysis tools are used to catch errors early.
- **Linting & Standards:** All code conforms to relevant linters (e.g., PEP8 for Python), and follows established conventions for readability and maintainability.
- **Documentation:** Functions and modules are documented with clear docstrings and comments.
- **Testing:** Unit and integration tests are written for all critical components, with a focus on coverage and edge cases.

## Technology-Agnostic Design with Databricks Connect Integration

While the framework is technology-agnostic, it demonstrates practical integration with Databricks Connect for scalable Spark DataFrame operations. This includes:

- **Chaining Dataframe Transformations:** Spark DataFrames are transformed using sequences of functional operations, leveraging the DataFrame `transform` method for modularity and clarity.
- **Reusable Utilities:** Utilities for data validation and transformation are compatible with Databricks Connect, but remain abstracted for portability.
- **AI-Driven Recommendations:** AI agents suggest improvements and generate utilities that integrate seamlessly with Databricks Connect.

## AI-Driven Guidance

AI agents enhance the project by:

- **Improving Test Coverage:** Automatically suggesting new data quality tests based on observed patterns and gaps.
- **Utility Creation:** Recommending and generating reusable utilities for common data engineering tasks.
- **Project Guidance:** Providing architectural recommendations, code reviews, and documentation updates to ensure best practices.

## Scalability and Maintainability

By combining functional programming with AI-driven insights and production-grade engineering practices, the framework supports scalable, maintainable solutions that adapt to changing requirements. The modular design enables rapid iteration and integration of new features, while the memory bank ensures that context is preserved across sessions.

## Usage

- Reference the memory bank for context before making architectural or implementation decisions.
- Implement data quality tests and utilities using functional programming principles and production-grade practices.
- Ensure each transformation function adheres to the single-responsibility principle and utilizes the DataFrame `transform` method for chaining.
- Leverage AI agents for recommendations, code generation, and documentation.
- Integrate with Databricks Connect for scalable Spark operations.
- Continuously update the memory bank to reflect project progress and decisions.

---

2025-10-17 13:38:11 - Enhanced project brief to emphasize DataFrame `transform` usage and single-responsibility principle in transformation logic.