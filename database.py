import sqlite3


def get_connection():
    conn = sqlite3.connect('high_score.db')
    return conn
