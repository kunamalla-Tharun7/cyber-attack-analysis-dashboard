"""
database_connection.py
Handles MySQL connection for Cyber Attack Analysis project.
Fully safe + .env compatible + Streamlit friendly.
"""

import os
import mysql.connector
from mysql.connector import Error
from dotenv import load_dotenv


# -----------------------------
# LOAD .ENV PROPERLY
# -----------------------------
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ENV_PATH = os.path.join(BASE_DIR, ".env")
load_dotenv(ENV_PATH)


# -----------------------------
# DATABASE CONFIG
# -----------------------------
DB_CONFIG = {
    "host": os.getenv("DB_HOST", "localhost"),
    "port": int(os.getenv("DB_PORT", 3306)),
    "user": os.getenv("DB_USER", "root"),
    "password": os.getenv("DB_PASSWORD", ""),  # MUST NOT BE EMPTY
    "database": os.getenv("DB_NAME", "cyber_attacks_analysis")
}


# -----------------------------
# GET CONNECTION
# -----------------------------
def get_connection():
    try:
        # Debug check (remove later if you want)
        if not DB_CONFIG["password"]:
            raise ValueError("❌ DB_PASSWORD is empty. Check your .env file")

        conn = mysql.connector.connect(**DB_CONFIG)

        if conn.is_connected():
            return conn

    except Error as e:
        raise RuntimeError(
            f"❌ MySQL connection failed at {DB_CONFIG['host']}:{DB_CONFIG['port']} -> {e}"
        )


# -----------------------------
# CLOSE CONNECTION
# -----------------------------
def close_connection(conn, cursor=None):
    try:
        if cursor:
            cursor.close()
        if conn and conn.is_connected():
            conn.close()
    except Exception:
        pass


# -----------------------------
# TEST CONNECTION
# -----------------------------
if __name__ == "__main__":
    conn = get_connection()
    print("✅ MySQL Connection Successful")
    close_connection(conn)