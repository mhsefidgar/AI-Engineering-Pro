# Project 01 — Production FastAPI API

Build a project-management API from an empty directory.

## Required stack

FastAPI, Pydantic, PostgreSQL, SQLAlchemy, Alembic, pytest, Docker.

## Features

- users and projects;
- CRUD with validation;
- pagination and filtering;
- authentication + authorization;
- idempotent create endpoint;
- database migrations;
- structured errors;
- health/readiness;
- request IDs;
- unit + integration + API tests;
- Docker Compose for local development.

## Milestones

1. Contract-first OpenAPI.
2. Schema + migration.
3. Repository/service/controller layers.
4. Auth boundary.
5. Tests and fixtures.
6. Operational instrumentation.
7. Containerization and CI.

## Stretch goals

Add Redis caching, background jobs, optimistic concurrency, and load testing.

## Definition of done

Another developer can clone the project, configure environment variables, start dependencies, run migrations, execute the test suite, and exercise documented endpoints without manual database edits.