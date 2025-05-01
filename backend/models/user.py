import os
import sqlite3

DATABASE_PATH = os.path.join(
    os.path.dirname(__file__),
    '..', 'database', 'nutrition_app.db'
)

def _get_conn():
    return sqlite3.connect(DATABASE_PATH)

def create_user_table():
    """Ensure the users table exists."""
    with _get_conn() as conn:
        conn.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id       INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT    NOT NULL UNIQUE,
                password TEXT    NOT NULL
            );
        ''')

def add_user_sql(username: str, hashed_password: str):
    """Raw SQL insert — no validation here."""
    with _get_conn() as conn:
        conn.execute('''
            INSERT INTO users (username, password)
            VALUES (?, ?)
        ''', (username, hashed_password))

def get_user_by_username_sql(username: str):
    """Raw SQL select — returns a tuple or None."""
    with _get_conn() as conn:
        cur = conn.execute(
            'SELECT id, username, password FROM users WHERE username = ?',
            (username,)
        )
        return cur.fetchone()

def get_user_by_id_sql(user_id: int):
    """Raw SQL select — returns a tuple or None."""
    with _get_conn() as conn:
        cur = conn.execute(
            'SELECT id, username, password FROM users WHERE id = ?',
            (user_id,)
        )
        return cur.fetchone()

