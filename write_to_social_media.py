import sqlite3

conn = sqlite3.connect("social")
cursor = conn.cursor()

add_users = """
INSERT INTO
    users(name, age, gender, nationality)
VALUES
    ('James', 25, 'male', 'USA'),
    ('Leila', 32, 'female', 'England'),
    ('Mike', 40, 'male', 'Denmark'),
    ('Elizabeth', 21, 'female', 'Canada')
"""

conn.execute(add_users)
