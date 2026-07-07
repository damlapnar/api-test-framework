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

---

## Test Architecture

### Why pytest?
pytest's fixture system enables session-scoped API clients (single login across a run) and function-scoped payload factories (fresh fake data per test). Parametrize decorators let one test method cover multiple data scenarios without code duplication.

### Design Decisions
| Decision | Choice | Rationale |
|----------|--------|-----------|
| Single `APIClient` class | `utils/api_client.py` | One place to change base URL, auth headers, and session config |
| Session-scoped auth | `conftest.py` `auth_token` fixture | Login once per test run; avoids repeated round-trips |
| Schema validation | `jsonschema` in `utils/schema_validator.py` | Contract tests catch breaking API changes before E2E suites do |
| Marker-based selection | `smoke`, `regression`, `users`, `auth` | CI runs `smoke` on every push; full `regression` on schedule |

### Test Pyramid
```
        ┌─────────────────────┐
        │ Contract/Schema Tests│  ← validate_schema() calls
        ├─────────────────────┤
        │ Integration Tests    │  ← Real HTTP against dummyjson.com
        └─────────────────────┘
```

### Adding a New Endpoint
1. Add test file under the relevant `tests/<domain>/` directory
2. Use `api_client` fixture for unauthenticated, `authenticated_client` for bearer-token flows
3. Run locally: `pytest tests/users/ -v`

### Running with Docker
```bash
docker build -t api-tests .
docker run --rm -v $(pwd)/reports:/app/reports api-tests
```
