## Description
Technical assessment: end-to-end data pipeline using Flask, FastAPI, and PostgreSQL, containerized with Docker.

## How to Run
docker-compose up -d

## API Endpoints

### Flask (Mock Server)
- GET /api/customers?page=1&limit=5
- GET /api/customers/{id}

### FastAPI (Pipeline)
- POST /api/ingest
- GET /api/customers?page=1&limit=5
- GET /api/customers/{id}

## Architecture
Flask (Mock API) → FastAPI (Ingestion) → PostgreSQL

## CD/CD
Added CI/CD pipeline using GitHub Actions. Now the project supports automated deployment to self-hosted runners, ensuring consistent environment and faster updates
