 ## Tech Stack:
1. Backend: Python (FastAPI or Flask)
2. Cloud: GCP (Cloud Functions, Pub/Sub, BigQuery, Firestore optional)
3. Containerization: Docker + Kubernetes
4. Database: BigQuery (main), optional Firestore for quick lookup
5. Version Control / CI-CD: GitHub + GitHub Actions


## Project Flow / Architecture:
1. Data Ingestion:
   1. Fetch data from public APIs. Examples:
   2. Flight data (e.g., OpenSky API)
   3. Weather data (OpenWeather API)
   4. COVID-19 or other public datasets
   5. Send the data to GCP Pub/Sub for asynchronous processing

2. Data Processing / ETL:
   1. A Python service (FastAPI) subscribes to Pub/Sub
   2. Clean, transform, and validate incoming data
   3. Store processed data in BigQuery for analytics

3. API Endpoints:
   1. Create REST endpoints to query summaries:
      1. Total number of records
      2. Daily trends or statistics
      3. Filter by specific criteria (location, time, etc.)

4. Containerization & Deployment:
   1. Dockerize the Python service
   2. Deploy in Kubernetes cluster
   3. Use GCP for managed services

5. Advanced Features:
   1. Automate the pipeline with Cloud Scheduler

Add alerting/logging for failed data ingestion

Add simple analytics dashboard using FastAPI + Plotly
