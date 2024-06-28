from flask import Flask, jsonify
import mysql.connector
from config import SQLConfig

app = Flask(__name__)

def connect_to_db():
    try:
        return mysql.connector.MySQLConnection(
            user=SQLConfig.USER,
            password=SQLConfig.PASSWORD,
            host=SQLConfig.HOST,
            database=SQLConfig.DATABASE,
            port=SQLConfig.PORT)
                                               
    except mysql.connector.Error as err:
        print(f"{err}")
        return None

cnx = connect_to_db()
cursor = cnx.cursor()
    
@app.route('/')
def hello():
    return 'Api de TUProfe!'

@app.route('/api/data/materias', methods=['GET'])
def get_materias():
    cursor.execute("select * from materias")
    resultados = cursor.fetchall()
    data = {
        'message': 'get de todas las materias',
        'status': 'success',
        'data': resultados
    }
    return jsonify(data)

@app.route('/api/data/materias/<id_materia>', methods=['GET'])
def get_materia(id_materia):
    # Aquí puedes retornar datos simulados como ejemplo
    cursor.execute(f"select * from materias where id_materia = %s", (id_materia,))
    resultados = cursor.fetchall()
    if resultados:
        data = {
            'message': 'Get de una materia con un plan especifico',
            'status': 'success',
            'data': resultados
        }
    else:    
        data = {
            'message': 'No se encontro la materia',
            'status': 'error',
            'data': []
        }
    return jsonify(data)

@app.route('/api/data/clientes', methods=['GET'])
def get_clientes():
    cursor.execute('select * from clientes')
    resultados = cursor.fetchall()
    if resultados:
        data = {
            'message': 'Get de todos los clientes',
            'status': 'success',
            'data': resultados
        }
    else:
        data = {
            'message': 'No se encontraron clientes',
            'status': 'error',
            'data': []
        }
    return jsonify(data)

@app.route('/api/data/clientes/<id_cliente>', methods=['GET'])
def get_cliente(id_cliente):
    cursor.execute(f"select * from clientes where id_cliente = %s", (id_cliente,))
    resultados = cursor.fetchall()
    if resultados:
        data = {
            'message': 'Get de un cliente especifico',
            'status': 'success',
            'data': resultados
        }
    else:
        data = {
            'message': 'No se encontro el cliente',
            'status': 'error',
            'data': []
        }
    return jsonify(data)
if __name__ == '__main__':
    app.run(debug=True)