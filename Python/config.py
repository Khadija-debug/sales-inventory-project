import os

# -----------------------
# PROJECT PATHS
# -----------------------

BASE_DIR = os.path.dirname(__file__)
DATASET_PATH = os.path.join(BASE_DIR, "..", "Dataset")
LOG_PATH = os.path.join(BASE_DIR, "..", "Logs")

# -----------------------
# SQL SERVER CONFIG
# -----------------------

SERVER = r".\SQLEXPRESS"
DATABASE = "olist_db"
DRIVER = "ODBC Driver 17 for SQL Server"

CONNECTION_STRING = (
    f"DRIVER={{{DRIVER}}};"
    f"SERVER={SERVER};"
    f"DATABASE={DATABASE};"
    "Trusted_Connection=yes;"
)