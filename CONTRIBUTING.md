# Contributing to api-test-framework

Thank you for your interest in contributing!

## Getting Started

```bash
git clone https://github.com/damlapinar/api-test-framework.git
cd api-test-framework
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Running Tests

```bash
pytest -m smoke
pytest -m regression
pytest -v
```

## Guidelines

- All tests must use the shared `api_client` fixture from `conftest.py`
- Add JSON schema files under `schemas/` for new response types
- Mark tests with appropriate markers: `@pytest.mark.smoke`, `@pytest.mark.regression`
- Avoid hardcoded test data — use `faker` fixtures

## Pull Request Process

1. Fork the repository
2. Create a feature branch (`git checkout -b feat/your-feature`)
3. Commit with a descriptive message
4. Open a Pull Request against `main`
5. Ensure all CI checks pass

## Reporting Bugs

Open a GitHub Issue with:
- Steps to reproduce
- Expected vs actual behavior
- Python version and OS
