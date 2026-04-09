# Github Actions Demo Repository

This repository demonstrates CI/CD patterns across multiple language ecosystems. It serves as a scaffolding example for build engineering.

## Project Structure

- `python/`: A User Management API built with FastAPI.
- `go/`: A Go-based microservice mirroring the user management logic.
- `.github/workflows/`: GitHub Action workflows for automated testing and building.

## Language Ecosystems

### Python
- **Framework**: FastAPI
- **Tests**: pytest
- **Workflow**: `.github/workflows/python-app.yml`

### Go
- **Framework**: Standard Library (`net/http`)
- **Tests**: Standard `testing` package
- **Workflow**: `.github/workflows/go-app.yml`
- **Build Tools**: Makefile, Dockerfile

## Build & Test

### Python
```bash
cd python
pip install -r requirements.txt
pytest tests
```

### Go
```bash
cd go
make test
make build
```
