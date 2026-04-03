import sqlite3

conn = sqlite3.connect('database1.db')
conn.row_factory = sqlite3.Row

users = conn.execute('SELECT * FROM users').fetchall()

if users:
    for user in users:
        print(f"ID: {user['id']}, Username: {user['username']}, Email: {user['email']}, Password: {user['password']}")
else:
    print("Aucun utilisateur dans la base.")

conn.close()