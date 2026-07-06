# API Test Framework

![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![pytest](https://img.shields.io/badge/pytest-0A9EDC?style=flat-square&logo=pytest&logoColor=white)
[![CI](https://github.com/damlapnar/api-test-framework/actions/workflows/api-tests.yml/badge.svg)](https://github.com/damlapnar/api-test-framework/actions/workflows/api-tests.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

REST API test framework built with Python and pytest. Features a reusable HTTP client, JSON schema validation, parallel execution, and CI/CD integration.

## Features

- **Reusable API Client** — session-based HTTP client with auth token support
- **JSON Schema Validation** — contract testing with jsonschema
- **Fixtures** — session-scoped API client and auth token
- **Parametrized Tests** — data-driven test cases
- **Parallel Execution** — `pytest-xdist` for faster runs
- **Markers** — `smoke`, `regression`, `auth`, `users` test suites
- **HTML Reports** — auto-generated after each run

## Project Structure

```
api-test-framework/
├── tests/
│   ├── users/        # User CRUD tests
│   └── auth/         # Authentication tests
├── fixtures/
│   └── conftest.py   # Shared fixtures
├── utils/
│   ├── api_client.py # HTTP client wrapper
│   └── schema_validator.py
├── schemas/          # JSON schema definitions
└── .github/workflows/
```

## Getting Started

```bash
python -m venv venv
source venv/bin/activate       # Windows: venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env
```

## Running Tests

```bash
# All tests
pytest

# Smoke tests only
pytest -m smoke

# Auth tests
pytest -m auth

# Parallel execution
pytest -n auto

# Specific test file
pytest tests/users/test_get_users.py -v
```
