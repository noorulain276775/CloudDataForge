import os
from fastapi import APIRouter, HTTPException
from app.models.data_model import DataBatch
from app.services.gcp_service import publish_to_pubsub, insert_to_bigquery

router = APIRouter(prefix="/pipeline", tags=["pipeline"])

@router.post("/process")
def process_data(batch: DataBatch):
    try:
        # Convert data to dict
        rows = [item.dict() for item in batch.items]
        
        if not rows:
            raise HTTPException(status_code=400, detail="No data items provided")

        # Publish messages to Pub/Sub
        pubsub_results = []
        for row in rows:
            try:
                result = publish_to_pubsub(str(row))
                pubsub_results.append({"status": "success", "message_id": result})
            except Exception as e:
                pubsub_results.append({"status": "error", "error": str(e)})

        # Insert into BigQuery using environment variable
        table_id = os.getenv("BIGQUERY_TABLE_ID", "my_table")  # fallback to my_table if not set
        bq_errors = insert_to_bigquery(table_id, rows)

        response = {
            "status": "success" if not bq_errors else "partial_success",
            "processed_count": len(rows),
            "pubsub_results": pubsub_results,
            "bigquery_errors": bq_errors if bq_errors else None
        }
        
        return response
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Processing failed: {str(e)}")
