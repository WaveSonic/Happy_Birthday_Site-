import sqlite3

DB_NAME = 'clickerV0.1.db'

# Підключення до бази даних
def get_db_connection():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    return conn

# Ініціалізація бази даних
def init_db():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            device_id TEXT PRIMARY KEY,
            username TEXT NOT NULL,
            clicks INTEGER DEFAULT 0,
            booster_modifier INTEGER DEFAULT 1
        )
    ''')
    conn.commit()
    conn.close()
