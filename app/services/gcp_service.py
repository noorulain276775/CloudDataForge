import os
from dotenv import load_dotenv
from google.cloud import pubsub_v1, bigquery

# Load environment variables
load_dotenv()

GCP_PROJECT_ID = os.getenv("GCP_PROJECT_ID")
GOOGLE_APPLICATION_CREDENTIALS = os.getenv("GOOGLE_APPLICATION_CREDENTIALS")
BIGQUERY_DATASET_ID = os.getenv("BIGQUERY_DATASET_ID")

if not GCP_PROJECT_ID:
    raise ValueError("GCP_PROJECT_ID not found in environment variables")

if not GOOGLE_APPLICATION_CREDENTIALS:
    raise ValueError("GOOGLE_APPLICATION_CREDENTIALS not found in environment variables")

if not BIGQUERY_DATASET_ID:
    raise ValueError("BIGQUERY_DATASET_ID not found in environment variables")

# Set the credentials environment variable
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = GOOGLE_APPLICATION_CREDENTIALS

# Initialize Pub/Sub publisher
publisher = pubsub_v1.PublisherClient()
topic_path = publisher.topic_path(GCP_PROJECT_ID, "data-topic")

# Initialize BigQuery client
bq_client = bigquery.Client(project=GCP_PROJECT_ID)
dataset_id = f"{GCP_PROJECT_ID}.{BIGQUERY_DATASET_ID}"

def publish_to_pubsub(message: str):
    """Publish a message to Pub/Sub"""
    try:
        message_bytes = message.encode("utf-8")
        future = publisher.publish(topic_path, message_bytes)
        return future.result()
    except Exception as e:
        print(f"Error publishing to Pub/Sub: {e}")
        raise

def insert_to_bigquery(table_id: str, rows: list):
    """Insert rows into BigQuery"""
    try:
        # Use the full table ID format
        full_table_id = f"{dataset_id}.{table_id}"
        errors = bq_client.insert_rows_json(full_table_id, rows)
        if errors:
            print("BigQuery insert errors:", errors)
        return errors
    except Exception as e:
        print(f"Error inserting to BigQuery: {e}")
        return [{"error": str(e)}]
