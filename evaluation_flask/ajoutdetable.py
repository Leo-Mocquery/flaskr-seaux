import sqlite3

# Chemin vers ta base de données
db_path = "database.db"  # Remplace par le vrai chemin, ex: "app.db"

conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Ajouter la colonne image_url si elle n'existe pas encore
try:
    cursor.execute("ALTER TABLE group_messages ADD COLUMN image_url TEXT;")
    print("Colonne 'image_url' ajoutée avec succès.")
except sqlite3.OperationalError as e:
    if "duplicate column name" in str(e):
        print("La colonne 'image_url' existe déjà, rien à faire.")
    else:
        raise e

conn.commit()
conn.close()