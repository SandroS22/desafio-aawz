import csv
import sqlite3

conn = sqlite3.connect('db-aawz')
cursor = conn.cursor()

with open('Vendas.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    next(reader)  # Pula o cabeçalho
    for row in reader:
        cursor.execute(
            "INSERT INTO vendas (dt_venda,nome_vendedor,valor_venda,tipo_cliente,canal_venda,custo_venda)"
            " VALUES (?, ?, ?, ?, ?, ?)",
            (row[1], row[2], row[3], row[4], row[5], row[6]))

conn.commit()

conn.close()
