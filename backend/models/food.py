import os
import sqlite3

DATABASE_PATH = os.path.join(os.path.dirname(__file__),
                             '..', 'database', 'nutrition_app.db')


def _get_conn():
    return sqlite3.connect(DATABASE_PATH)


def create_food_table():
    with _get_conn() as conn:
        conn.execute('''
          CREATE TABLE IF NOT EXISTS foods (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            serving_size REAL NOT NULL,
            calories INTEGER NOT NULL,
            protein REAL NOT NULL,
            carbs REAL NOT NULL,
            fat REAL NOT NULL
          );
        ''')


def add_food(name, serving_size, calories, protein, carbs, fat):
    with _get_conn() as conn:
        conn.execute('''
          INSERT INTO foods (name, serving_size, calories, protein, carbs, fat)
          VALUES (?, ?, ?, ?, ?, ?)
        ''', (name, serving_size, calories, protein, carbs, fat))


def get_foods():
    with _get_conn() as conn:
        return conn.execute('SELECT * FROM foods').fetchall()


def update_food(food_id, name, serving_size, calories, protein, carbs, fat):
    with _get_conn() as conn:
        conn.execute('''
          UPDATE foods
          SET name = ?, serving_size = ?, calories = ?, protein = ?, carbs = ?, fat = ?
          WHERE id = ?
        ''', (name, serving_size, calories, protein, carbs, fat, food_id))


def delete_food(food_id):
    with _get_conn() as conn:
        conn.execute('DELETE FROM foods WHERE id = ?', (food_id,))
