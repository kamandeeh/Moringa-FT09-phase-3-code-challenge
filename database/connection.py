import sqlite3

def get_db_connection():
    conn = sqlite3.connect("magazine.db")
    conn.row_factory = sqlite3.Row  # Return rows as dictionary-like objects
    return conn
