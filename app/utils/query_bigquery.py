"""
BigQuery Query Utility
Run SQL queries against your BigQuery tables
"""

import os
from dotenv import load_dotenv
from google.cloud import bigquery

# Load environment variables
load_dotenv()

# Get configuration
GCP_PROJECT_ID = os.getenv("GCP_PROJECT_ID")
GOOGLE_APPLICATION_CREDENTIALS = os.getenv("GOOGLE_APPLICATION_CREDENTIALS")
BIGQUERY_DATASET_ID = os.getenv("BIGQUERY_DATASET_ID")
BIGQUERY_TABLE_ID = os.getenv("BIGQUERY_TABLE_ID")

# Set credentials
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = GOOGLE_APPLICATION_CREDENTIALS

# Initialize BigQuery client
client = bigquery.Client(project=GCP_PROJECT_ID)

def run_query(sql_query):
    """Run a SQL query and return results"""
    try:
        results = client.query(sql_query)
        return results
    except Exception as e:
        print(f"Error running query: {e}")
        return None

def show_table_info():
    """Show basic table information"""
    table_id = f"{GCP_PROJECT_ID}.{BIGQUERY_DATASET_ID}.{BIGQUERY_TABLE_ID}"
    print(f"=== Table Information ===")
    print(f"Project: {GCP_PROJECT_ID}")
    print(f"Dataset: {BIGQUERY_DATASET_ID}")
    print(f"Table: {BIGQUERY_TABLE_ID}")
    print(f"Full Table ID: {table_id}")
    print()

def show_all_data(limit=10):
    """Show all data in the table"""
    table_id = f"{GCP_PROJECT_ID}.{BIGQUERY_DATASET_ID}.{BIGQUERY_TABLE_ID}"
    query = f"SELECT * FROM `{table_id}` ORDER BY value DESC LIMIT {limit}"
    
    print(f"=== All Data (Top {limit}) ===")
    results = run_query(query)
    if results:
        for row in results:
            print(f"Name: {row.name}, Value: {row.value}")
    print()

def show_count():
    """Show total row count"""
    table_id = f"{GCP_PROJECT_ID}.{BIGQUERY_DATASET_ID}.{BIGQUERY_TABLE_ID}"
    query = f"SELECT COUNT(*) as total_rows FROM `{table_id}`"
    
    print("=== Row Count ===")
    results = run_query(query)
    if results:
        for row in results:
            print(f"Total rows: {row.total_rows}")
    print()

def show_stats():
    """Show basic statistics"""
    table_id = f"{GCP_PROJECT_ID}.{BIGQUERY_DATASET_ID}.{BIGQUERY_TABLE_ID}"
    query = f"""
    SELECT 
        COUNT(*) as total_rows,
        MIN(value) as min_value,
        MAX(value) as max_value,
        AVG(value) as avg_value
    FROM `{table_id}`
    """
    
    print("=== Statistics ===")
    results = run_query(query)
    if results:
        for row in results:
            print(f"Total rows: {row.total_rows}")
            print(f"Min value: {row.min_value}")
            print(f"Max value: {row.max_value}")
            print(f"Average value: {row.avg_value:.2f}")
    print()

def show_recent_data(hours=1):
    """Show recent data (if you have timestamp column)"""
    table_id = f"{GCP_PROJECT_ID}.{BIGQUERY_DATASET_ID}.{BIGQUERY_TABLE_ID}"
    # Note: This assumes you have a timestamp column. Adjust as needed.
    query = f"SELECT * FROM `{table_id}` ORDER BY name DESC LIMIT 5"
    
    print(f"=== Recent Data (Last 5 entries) ===")
    results = run_query(query)
    if results:
        for row in results:
            print(f"Name: {row.name}, Value: {row.value}")
    print()

def custom_query(sql_query):
    """Run a custom SQL query"""
    print(f"=== Custom Query ===")
    print(f"SQL: {sql_query}")
    print("Results:")
    results = run_query(sql_query)
    if results:
        for row in results:
            print(row)
    print()

if __name__ == "__main__":
    print("🔍 BigQuery Query Utility")
    print("=" * 50)
    
    # Show table information
    show_table_info()
    
    # Show basic statistics
    show_count()
    show_stats()
    
    # Show recent data
    show_recent_data()
    
    # Show all data
    show_all_data(10)
    
    # Example custom queries
    print("=== Example Custom Queries ===")
    
    # Query 1: Find specific values
    table_id = f"{GCP_PROJECT_ID}.{BIGQUERY_DATASET_ID}.{BIGQUERY_TABLE_ID}"
    custom_query(f"SELECT * FROM `{table_id}` WHERE value > 5")
    
    # Query 2: Group by name
    custom_query(f"SELECT name, COUNT(*) as count FROM `{table_id}` GROUP BY name")
    
    # Query 3: Find pipeline_test entries
    custom_query(f"SELECT * FROM `{table_id}` WHERE name LIKE '%pipeline%'")
