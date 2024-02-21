from flask import Flask, make_response, jsonify, request
from bd import Carros

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False
port = 5000

@app.route('/', methods=['GET'])
def get_ping():
    return "Server running on port :%i" % port

@app.route('/carros', methods=['GET'])
def get_carros():
    return make_response(
        jsonify(
            message = 'Lista de carros',
            dados = Carros )
        )

@app.route('/carros', methods=['POST'])
def create_carro():
    carro = request.json
    Carros.append(carro)
    return make_response(
        jsonify(
            message = 'Carro cadastrado com sucesso',
            carro = carro )
        )

app.run(port=port)