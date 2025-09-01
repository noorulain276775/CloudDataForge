import os
from dotenv import load_dotenv
from google.cloud import bigquery

# Load environment variables
load_dotenv()

GCP_PROJECT_ID = os.getenv("GCP_PROJECT_ID")
GOOGLE_APPLICATION_CREDENTIALS = os.getenv("GOOGLE_APPLICATION_CREDENTIALS")
BIGQUERY_DATASET_ID = os.getenv("BIGQUERY_DATASET_ID")
BIGQUERY_TABLE_ID = os.getenv("BIGQUERY_TABLE_ID")

if not GCP_PROJECT_ID:
    raise ValueError("GCP_PROJECT_ID not found in environment variables")

if not GOOGLE_APPLICATION_CREDENTIALS:
    raise ValueError("GOOGLE_APPLICATION_CREDENTIALS not found in environment variables")

if not BIGQUERY_DATASET_ID:
    raise ValueError("BIGQUERY_DATASET_ID not found in environment variables")

if not BIGQUERY_TABLE_ID:
    raise ValueError("BIGQUERY_TABLE_ID not found in environment variables")

# Set the credentials environment variable
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = GOOGLE_APPLICATION_CREDENTIALS

client = bigquery.Client(project=GCP_PROJECT_ID)

# Use environment variables for dataset and table names
dataset_id = f"{GCP_PROJECT_ID}.{BIGQUERY_DATASET_ID}"
table_id = f"{dataset_id}.{BIGQUERY_TABLE_ID}"

# Define schema explicitly
schema = [
    bigquery.SchemaField("name", "STRING", mode="REQUIRED"),
    bigquery.SchemaField("value", "FLOAT", mode="REQUIRED"),
]

def create_table():
    try:
        # First, ensure the dataset exists
        dataset_ref = bigquery.Dataset(dataset_id)
        dataset = client.create_dataset(dataset_ref, exists_ok=True)
        print(f"Dataset {dataset_id} ready.")
        
        # Check if table exists
        try:
            existing_table = client.get_table(table_id)
            print(f"Table {table_id} already exists with schema.")
            return True
        except Exception:
            # Table doesn't exist, create it
            print(f"Table {table_id} doesn't exist, creating it...")
            table = bigquery.Table(table_id, schema=schema)
            table = client.create_table(table)
            print(f"Table {table_id} created with schema.")
            return True
        
    except Exception as e:
        print(f"Error creating table: {e}")
        return False

def insert_bulk_data(n=10):
    try:
        # Test with smaller dataset first
        bulk_rows = [{"name": f"User{i}", "value": float(i)} for i in range(n)]
        print(f"Attempting to insert {len(bulk_rows)} rows...")
        print(f"Sample row: {bulk_rows[0]}")
        errors = client.insert_rows_json(table_id, bulk_rows)
        if errors:
            print("Errors:", errors)
            return False
        else:
            print(f"Inserted {n} rows successfully.")
            return True
    except Exception as e:
        print(f"Error inserting data: {e}")
        return False

if __name__ == "__main__":
    print(f"Using dataset: {dataset_id}")
    print(f"Using table: {table_id}")
    
    # Create table if it doesn't exist
    if create_table():
        # Insert data
        insert_bulk_data(10)
    else:
        print("Failed to create table, skipping data insertion.")
