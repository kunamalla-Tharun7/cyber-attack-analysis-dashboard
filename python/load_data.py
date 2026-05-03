import os
import mysql.connector
from mysql.connector import Error
from dotenv import load_dotenv


# -----------------------------
# FORCE CORRECT .ENV PATH
# -----------------------------
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ENV_PATH = os.path.join(BASE_DIR, ".env")

print("🔍 Loading .env from:", ENV_PATH)  # DEBUG LINE

load_dotenv(dotenv_path=ENV_PATH)


# -----------------------------
# READ VARIABLES
# -----------------------------
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_NAME = os.getenv("DB_NAME")


# -----------------------------
# DEBUG CHECK (IMPORTANT)
# -----------------------------
print("DB_HOST:", DB_HOST)
print("DB_USER:", DB_USER)
print("DB_PASSWORD:", DB_PASSWORD)


# -----------------------------
# CONNECTION
# -----------------------------
def get_connection():
    if not DB_PASSWORD:
        raise RuntimeError("❌ DB_PASSWORD NOT LOADED. Check .env file location")

    try:
        conn = mysql.connector.connect(
            host=DB_HOST,
            port=int(DB_PORT or 3306),
            user=DB_USER,
            password=DB_PASSWORD,
            database=DB_NAME
        )
        return conn

    except Error as e:
        raise RuntimeError(f"MySQL connection failed: {e}")


def close_connection(conn, cursor=None):
    if cursor:
        cursor.close()
    if conn:
        conn.close()


if __name__ == "__main__":
    conn = get_connection()
    print("✅ Connection successful")
    close_connection(conn)