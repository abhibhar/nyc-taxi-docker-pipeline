# NYC Taxi Ingestion Pipeline (Docker + Postgres)

Loads 1.37M NYC Yellow Taxi trips (Jan 2021) into PostgreSQL using a containerized Python pipeline.

## Architecture
Public CSV -> ingest container (pandas, 100k-row chunks) -> Postgres container -> persistent volume

## Run it
    docker compose up -d mydb
    docker compose run --rm ingest
    docker compose exec mydb psql -U root -d sales -c "SELECT COUNT(*) FROM yellow_taxi;"

## Key decisions
- Chunked loading (100k rows) keeps memory flat regardless of file size
- Date columns parsed to TIMESTAMP before loading, not stored as text
- Named volume so data survives container restarts
- Services talk over the Compose network by service name (mydb), not localhost

## Files
| File | Purpose |
|---|---|
| docker-compose.yml | Postgres + loader + ingest services |
| ingest.py / Dockerfile.ingest | Main pipeline: chunked load of 1.37M rows |
| explore.py | Data profiling: inspect sample and fix types |
| load.py / Dockerfile.load | Small loader used to learn container networking |
| app.py / Dockerfile | First Docker exercise: parameterized script + volumes |
