from flask import Flask, jsonify
import mysql.connector
app = Flask(__name__)

def connect_to_db():
    try:
        return mysql.connector.MySQLConnection(
            user='root',
            password='',
            host='localhost',
            database='tuprofe',
            port='3306')
                                               
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

if __name__ == '__main__':
    app.run(debug=True)