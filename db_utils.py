import sqlite3
import pandas as pd

def create_connection(db_path):
    """Create a database connection to the SQLite database."""
    conn = sqlite3.connect(db_path)
    return conn

def create_table(conn):
    """Create the weather table if it doesn't exist."""
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS weather (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT,
            temperature REAL,
            humidity REAL
        )
    """)
    conn.commit()
