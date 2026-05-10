import sqlite3

def get_user(username):
    conn = sqlite3.connect("users.db")
    query = f"SELECT * FROM users WHERE name = '{username}'"
    conn.execute(query)

SECRET_KEY = "hardcoded_secret_12345"