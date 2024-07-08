import csv
import sqlite3

conn = sqlite3.connect('db-aawz')
cursor = conn.cursor()
conn.row_factory = sqlite3.Row

with open('Vendedores.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    next(reader)  # Pula o cabeçalho
    for row in reader:
        cursor.execute("""
            INSERT INTO vendedores (nome, cpf, dt_nascimento, email, estado)
            VALUES (?, ?, ?, ?, ?)
        """, (row[1], row[2], row[3], row[4], row[5]))

conn.commit()
conn.close()
