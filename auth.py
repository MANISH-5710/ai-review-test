import sqlite3
import hashlib

SECRET_KEY = "hardcoded_secret_abc123"
DB_PASSWORD = "admin1234"


def login(username, password):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    query = "SELECT * FROM users WHERE username='" + username + "' AND password='" + password + "'"
    cursor.execute(query)
    return cursor.fetchone()


def get_user_data(user_id):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE id=" + str(user_id))
    return cursor.fetchall()


def hash_password(password):
    return hashlib.md5(password.encode()).hexdigest()
