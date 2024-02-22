import mysql.connector
from flask import Flask, make_response, jsonify, request
from bd import Carros

mydb = mysql.connector.connect(
    host='localhost',
    user='ed',
    password='ed',
    database='db'
)
app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False
port = 5000

@app.route('/', methods=['GET'])
def get_ping():
    return "Server running on port :%i" % port

@app.route('/carros', methods=['GET'])
def get_carros():
    my_cursor = mydb.cursor()

    my_cursor.execute('SELECT * FROM carros')

    meus_carros = my_cursor.fetchall()
    carros = list()
    for carro in meus_carros:
        carros.append(
            {
                'id': carro[0],
                'marca': carro[1],
                'modelo': carro[2],
                'ano': carro[3]
            }
        )

    return make_response(
        jsonify(
            message = 'Lista de carros',
            dados = carros )
        )

@app.route('/carros', methods=['POST'])
def create_carro():
    carro = request.json

    my_cursor = mydb.cursor()
    sql = f"INSET INTO carros (marca, modelo, ano) VALUES ('{carro['marca']}', '{carro['modelo']}', {carro['ano']})"
    my_cursor.execute(sql)
    mydb.commit()
    
    return make_response(
        jsonify(
            message = 'Carro cadastrado com sucesso',
            carro = carro )
        )

app.run(port=port)