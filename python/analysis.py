import pandas as pd
from database_connection import get_connection

def fetch_data(query):
    conn = get_connection()
    df = pd.read_sql(query, conn)
    conn.close()
    return df


def top_countries():
    return fetch_data("""
        SELECT country, COUNT(*) AS attacks
        FROM cyber_attacks
        GROUP BY country
        ORDER BY attacks DESC
        LIMIT 10
    """)


def top_industries():
    return fetch_data("""
        SELECT industry, COUNT(*) AS attacks
        FROM cyber_attacks
        GROUP BY industry
        ORDER BY attacks DESC
        LIMIT 10
    """)


def yearly_trend():
    return fetch_data("""
        SELECT year, COUNT(*) AS attacks
        FROM cyber_attacks
        GROUP BY year
        ORDER BY year
    """)


def financial_loss():
    return fetch_data("""
        SELECT attack_type, SUM(financial_loss) AS loss
        FROM cyber_attacks
        GROUP BY attack_type
        ORDER BY loss DESC
    """)