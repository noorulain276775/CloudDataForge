from fastapi import FastAPI
from dotenv import load_dotenv
import os

load_dotenv()  # Load .env variables

GCP_PROJECT_ID = os.getenv("GCP_PROJECT_ID")

app = FastAPI()

@app.get("/")
def read_root():
    
    return {"message": f"GCP Project ID is {GCP_PROJECT_ID}"}

# Import and include pipeline routes
from .routes.pipelines import router as pipeline_router
app.include_router(pipeline_router)
