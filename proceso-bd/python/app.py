from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

def crear_tabla():
    connection = sqlite3.connect('facultad.db')
    cursor = connection.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS docentes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            materia TEXT NOT NULL,
            horas_catedras INTEGER NOT NULL
        )
    ''')
    connection.commit()
    connection.close()

crear_tabla()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/agregar', methods=['POST'])
def agregar():
    if request.method == 'POST':
        nombre = request.form['nombre']
        materia = request.form['materia']
        horas_catedras = request.form['horas_catedras']

        conn = sqlite3.connect('facultad.db')
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO docentes (nombre, materia, horas_catedras)
            VALUES (?, ?, ?)
        ''', (nombre, materia, horas_catedras))
        
        conn.commit()
        conn.close()

        return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)