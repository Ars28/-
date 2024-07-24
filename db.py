import sqlite3

connection = sqlite3.connect('Slaves.db')
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
user_id INTEGER PRIMARY KEY,
phone TEXT NOT NULL,
mail TEXT NOT NULL,
telegram TEXT NOT NULL,
information TEXT NOT NULL,
skills TEXT NOT NULL
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS projects (
project_id INTEGER PRIMARY KEY,
name TEXT NOT NULL,
idea TEXT NOT NULL,
needed_skills TEXT NOT NULL,
information TEXT NOT NULL,
active INTEGER NOT NULL
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS teams (
team_id INTEGER PRIMARY KEY,
user_id INTEGER REFERENCES users(user_id),
project_id INTEGER REFERENCES projects(project_id),
age INTEGER
)
''')

connection.commit()
connection.close()