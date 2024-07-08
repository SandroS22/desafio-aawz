import sqlite3

from flask import jsonify

from Enumerators.TipoEstado import TipoEstado

# ATUALIZAR
DATABASE = "PATH PARA O BANCO DE DADOS"


def get_db():
    db = sqlite3.connect(DATABASE)
    db.row_factory = sqlite3.Row
    return db


def get_vendedor(id_vendedor: int):
    try:
        db = get_db()
        cursor = db.cursor()
        cursor.execute("SELECT * FROM vendedores WHERE id = ?", (id_vendedor,))
        dados = cursor.fetchall()
        if len(dados) == 0:
            return jsonify({'error': 'Vendedor não encontrado'})
        db.close()
        return jsonify(dict(dados[0]))
    except sqlite3.Error as e:
        return jsonify({'error': str(e)}), 500


def get_vendedores():
    try:
        db = get_db()
        cursor = db.cursor()
        cursor.execute("SELECT * FROM vendedores")
        dados = cursor.fetchall()
        db.close()
        return jsonify([dict(row) for row in dados])
    except sqlite3.Error as e:
        return jsonify({'error': str(e)}), 500


def cadastrar_vendedor(nome: str, cpf: str, email: str, dt_nascimento: str, estado: TipoEstado):
    try:
        db = get_db()
        cursor = db.cursor()
        cursor.execute("INSERT INTO vendedores (nome, cpf, email, dt_nascimento, estado) VALUES (?, ?, ?, ?, ?)",
                       (nome, cpf, email, dt_nascimento, estado))
        db.commit()
        db.close()
        return jsonify({'message': 'Vendedor criado com sucesso!'}), 201
    except sqlite3.Error as e:
        return jsonify({'error': str(e)}), 500


def apagar_vendedor(id_vendedor: int):
    try:
        db = get_db()
        cursor = db.cursor()
        vendedor = get_vendedor(id_vendedor)
        if 'error' in vendedor.json:
            return vendedor
        cursor.execute("DELETE FROM vendedores WHERE id = ?", (id_vendedor,))
        db.commit()
        db.close()
        return jsonify({'message': 'Vendedor apagado com sucesso!'}), 200
    except sqlite3.Error as e:
        return jsonify({'error': str(e)}), 500


def vendas():
    try:
        db = get_db()
        cursor = db.cursor()
        cursor.execute("SELECT * FROM vendas")
        dados = cursor.fetchall()
        db.close()
        return jsonify([dict(row) for row in dados])
    except sqlite3.Error as e:
        return jsonify({'error': str(e)}), 500
