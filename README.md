# Health App

Author: Nikodem Denega

A health and BMI tracker API built with FastAPI, managed by Poetry, and containerized using Docker.

## Project Structure
* `src/health_app/health.py` - Core business logic for BMI and weight calculations.
* `src/health_app/data.py` - Persistence layer handling JSON file operations.
* `src/health_app/api.py` - FastAPI application exposing the endpoints.
* `tests/` - Unit tests for the application logic and data layers.

## Setup and Testing Locally

1. **Install Dependencies:**
   Make sure you have Poetry installed, then run:
   ```
   python -m poetry install
   ```
Run Unit Tests:
:

```
python -m poetry run pytest tests/ -v
```

**Docker Configuration**
```
docker compose up
```

**API Endpoints**

GET / - Health check endpoint verifying the API status.

GET /records - Retrieves a list of all saved health records from the persistent store.

POST /records - Creates a new health record, dynamically calculates BMI metrics, saves it, and returns the complete object.

**Example Curl Commands**
You can use the following commands to interact with the API once the application is running (locally or inside Docker):

1. Health Check:
```
curl http://localhost:8000/
```
2. List All Records:
```
curl http://localhost:8000/records
```
4. Add a New Record:
```
curl -X POST http://localhost:8000/records \
  -H "Content-Type: application/json" \
  -d '{"name":"Nikodem","weight_kg":100,"height_m":1.85}'
```
