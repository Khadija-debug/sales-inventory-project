import logging
import os
import time
from datetime import datetime


from extract import extract_data
from transform import transform_data
from validation import validate_data
from load import load_data

# -----------------------
# LOGGING SETUP
# -----------------------
LOG_DIR = os.path.join(os.path.dirname(__file__), "..", "Logs")
os.makedirs(LOG_DIR, exist_ok=True)

logging.basicConfig(
    filename=os.path.join(LOG_DIR, "etl.log"),
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# -----------------------
# ETL PIPELINE WITH ERROR HANDLING
# -----------------------
start_time =time.time()
start_datetime = datetime.now()
print(f" time started at: {start_datetime.strftime('%Y-%m-%d %H:%M:%S')}")
print("🚀 FULL ETL PIPELINE STARTED")
logging.info("ETL Pipeline Started")

try:
    # Extract
    print("📥 Extracting data...")
    orders, customers, products, order_items, payments, reviews, sellers = extract_data()
    logging.info("Extract completed successfully")

    # Transform
    print("🔄 Transforming data...")
    orders_clean = transform_data(orders)
    logging.info("Transform completed successfully")

    # Validate
    print("✅ Validating data...")
    validate_data(orders_clean, customers, products)
    logging.info("Validation completed successfully")

    # Load
    print("📤 Loading data...")
    load_data(orders_clean, customers, products, order_items, payments, reviews, sellers)
    logging.info("Load completed successfully")

    print("🎉 ETL PIPELINE COMPLETED SUCCESSFULLY")
    end_time = time.time()
    end_datetime = datetime.now()
    duration =round(end_time - start_time, 2)
    print (f" time finished at: {end_datetime.strftime('%Y-%m-%d %H:%M:%S')}")
    print (f"Total Execution Time: {duration} seconds")
    logging.info(f"Execution Time: {duration} seconds")
    logging.info("ETL Pipeline Completed Successfully")

except Exception as e:
    print("❌ ETL PIPELINE FAILED")
    print(str(e))
    logging.error(f"ETL Pipeline Failed: {str(e)}")