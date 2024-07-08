from flask import Flask, request, jsonify

from Controllers.AppController import AppController
from Enumerators.CanalVenda import CanalVenda
from Enumerators.TipoEstado import TipoEstado

app = Flask(__name__)

ctrl = AppController()


@app.route('/vendedores')
def get_vendedores():
    return ctrl.get_vendedores()


@app.route('/')
def home():
    return "Bem vindo!"


@app.route('/vendedores/novo_vendedor', methods=['POST', 'GET'])
def cadastrar_vendedor():
    if request.method == 'POST':
        dados = request.json
        if dados.get('dt_nascimento') is None or dados.get('nome') is None or dados.get('email') is None or dados.get(
                'cpf') is None or dados.get('estado') is None:
            return jsonify({'error': 'Informe todos os dados!'})
        nome = dados['nome']
        email = dados['email']
        dt_nascimento = dados['dt_nascimento']
        cpf = dados['cpf']
        estado = dados['estado']
        return ctrl.cadastrar_vendedor(nome, cpf, email, dt_nascimento, estado)
    elif request.method == 'GET':
        return home()


@app.route('/vendedor', methods=['POST', 'GET'])
def get_vendedor():
    if request.method == 'POST':
        dados = request.json
        if dados.get('id_vendedor') is None:
            return jsonify({'error': 'Informe o ID do vendedor!'})
        id = int(dados['id_vendedor'])
        return ctrl.get_vendedor(id)
    elif request.method == 'GET':
        return home()


@app.route('/vendedores/apagar_vendedor', methods=['DELETE', 'GET'])
def apagar_vendedor():
    if request.method == 'DELETE':
        dados = request.json
        if dados.get('id_vendedor') is None:
            return jsonify({'error': 'Informe o ID do vendedor!'})
        id = int(dados['id_vendedor'])
        return ctrl.apagar_vendedor(id)
    elif request.method == 'GET':
        return home()


@app.route('/comissoes', methods=['GET'])
def comissoes():
    vendedores = ctrl.calcula_comissao()
    return jsonify(vendedores)


if __name__ == '__main__':
    app.run()
