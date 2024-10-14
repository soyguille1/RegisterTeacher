import sqlite3

conn = sqlite3.connect('facultad.db')
cursor = conn.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS docentes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        materia TEXT NOT NULL,
        horas_catedras INTEGER NOT NULL
    )
''')
conn.commit()
conn.close()        