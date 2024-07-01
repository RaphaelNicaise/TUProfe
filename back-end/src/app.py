from flask import Flask, jsonify, request
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
            port=SQLConfig.PORT
        )
                                               
    except mysql.connector.Error as err:
        print(f"{err}")
        return None

cnx = connect_to_db()
cursor = cnx.cursor()
    
@app.route('/')
def rutas_menu():
    # retornar todas las rutas posibles
    return jsonify({
        'message': 'Bienvenido a la API de la Universidad, la api esta funcionando correctamente',
        'status': 'success',
        'data': {
            'rutas': [
                '/api/data/materias',
                '/api/data/materias/<id_materia>',
                '/api/data/clientes',
                '/api/data/clientes/<id_cliente>',
                '/api/data/profesores',
                '/api/data/profesores/<id_profesor>'
            ]
        }
    })

@app.route('/api/data/materias', methods=['GET'])
def get_materias():
    try:
        cnx = connect_to_db()
        cursor = cnx.cursor(dictionary=True)
        cursor.execute("select * from materias")
        resultados = cursor.fetchall()
    except mysql.connector.Error as err:
        print(f"{err}")
    finally:
        cursor.close()
        cnx.close()
        if resultados:
            data = {
                'message': 'get de todas las materias','status': 'success','data': resultados} 
            return jsonify(data)
        else:
            return jsonify({
                'message': 'No se encontraron las materias', 'status': 'error','data': []}), 404
            

@app.route('/api/data/materias/<id_materia>', methods=['GET'])
def get_materia(id_materia):
    # Aquí puedes retornar datos simulados como ejemplo
    try:
        cnx = connect_to_db()
        cursor = cnx.cursor(dictionary=True)
        cursor.execute(f"select * from materias where id_materia = %s", (id_materia,))
        resultados = cursor.fetchall()
    except mysql.connector.Error as err:
         print(f"{err}")
    finally:    
        cursor.close()
        cnx.close()
        if resultados:
            data = {
                'message': 'Get de una materia con un plan especifico','status': 'success','data': resultados
            }
            return jsonify(data)
        else:    
            return jsonify({
                'message': 'No se encontró la materia','status': 'error','data': []}), 404
        

@app.route('/api/data/clientes', methods=['GET', 'POST'])
def clientes():
    if request.method == 'GET':
        try:  
            cnx = connect_to_db()
            cursor = cnx.cursor(dictionary=True)
            cursor.execute('select * from clientes')
            resultados = cursor.fetchall()
        except mysql.connector.Error as err:
            print(f"{err}")
        finally:
            cursor.close()
            cnx.close()
            if resultados:
                data = {
                    'message': 'Get de todos los clientes','status': 'success','data': resultados
                }
                return jsonify(data)
            else:
                return jsonify({
                    'message': 'No se encontraron clientes','status': 'error', 'data': []}), 404
                
    elif request.method == 'POST': # INSERTAR CLIENTE
        try:
            cnx = connect_to_db()
            cursor = cnx.cursor(dictionary=True)
            if request.headers['Content-Type'] != 'application/json': # CHEQUEA QUE EL CONTENT TYPE SEA JSON
                return jsonify({
                'message': 'Tipo de contenido no soportado. Asegúrate de enviar JSON.',
                'status': 'error'
                    }), 415
                
            data = request.json # RECOLECTA LOS DATOS DEL JSON, Y LOS GUARDA EN VARIABLES
            nombre = data.get('nombre', '')
            apellido = data.get('apellido', '')
            correo = data.get('correo', '')
            telefono = data.get('telefono', '')
            descripcion = data.get('descripcion', '')  
            # LLAMA AL PROCEDIMIENTO INSERT_CLIENTE, Y LE PASA LOS DATOS
            cursor.callproc('insert_cliente', (nombre, apellido, correo, telefono, descripcion)) 
            cnx.commit()
        
            return jsonify({
                'message': 'Cliente creado exitosamente','status': 'success','data': data}), 201 
            # CODIGO 201 DE RESPUESTA DE EXITO Y CREACION DE RECURSO
        
        except mysql.connector.Error as err:
            print(f"Error al crear cliente: {err}")
            return jsonify({
                'message': 'Error al crear cliente','status': 'error','data': []}), 500
        
        finally:
            cursor.close()
            cnx.close()        

            
@app.route('/api/data/clientes/<id_cliente>', methods=['GET'])
def get_cliente(id_cliente):
    try:
        cnx = connect_to_db()
        cursor = cnx.cursor(dictionary=True)
        cursor.execute(f"select * from clientes where id_cliente = %s", (id_cliente,))
        resultados = cursor.fetchall()
    except mysql.connector.Error as err:
        print(f"{err}")
    finally:    
        cursor.close()
        cnx.close()
        if resultados:
            data = {
                'message': 'Get de un cliente especifico','status': 'success','data': resultados
            }
            return jsonify(data)
        else:
            return jsonify({
                'message': 'No se encontraron al cliente','status': 'error','data': []}), 404

       
@app.route('/api/data/profesores', methods=['GET'])
def get_profesores():
    try:
        cnx = connect_to_db()
        cursor = cnx.cursor(dictionary=True)
        cursor.execute('select * from profesores')
        resultados = cursor.fetchall()
    except mysql.connector.Error as err:
        print(f"{err}")
    finally:
        cursor.close()
        cnx.close()
        if resultados:
            data = {
                'message': 'Get de todos los profesores',
                'status': 'success',
                'data': resultados
            }
            return jsonify(data)
        else:
            return jsonify({
                'message': 'No se encontraron profesores','status': 'error','data': []}), 404

    
@app.route('/api/data/profesores/<id_profesor>', methods=['GET'])
def get_profesor(id_profesor):
    try:
        cnx = connect_to_db()
        cursor = cnx.cursor(dictionary=True)
        cursor.execute(f"select * from profesores where id_profesor = %s", (id_profesor,))
        resultados = cursor.fetchall()
    except mysql.connector.Error as err:
        print(f"{err}")
    finally:
        cursor.close()
        cnx.close()
        if resultados:
            data = {
                'message': 'Get de un profesor especifico','status': 'success','data': resultados
            }
            return jsonify(data)
        else:
            return jsonify({
                'message': 'No se encontró al profesor','status': 'error','data': []}), 404


# ENDPOINT PARA MANDAR FEEDBACK DE UN PROFESOR, MEDIANTE UN POST
@app.route('/api/data/sendfeedback', methods=['POST'])
def sendfeedback():
    try:
        cnx = connect_to_db()
        cursor = cnx.cursor(dictionary=True)
        if request.headers['Content-Type'] != 'application/json':
            return jsonify({
                'message': 'Tipo de contenido no soportado. Asegúrate de enviar JSON.','status': 'error'}), 415
        # OBTENEMOS LOS DATOS DE REACT
        data = request.json
        id_profesor = data.get('id_profesor', '')
        id_cliente = data.get('id_cliente', '')
        comentario = data.get('comentario', '')
        claridad_profesor_calif = data.get('claridad_profesor_calif', '')
        precio_profesor_calif = data.get('precio_profesor_calif', '')
        disponibilidad_profesor_calif = data.get('disponibilidad_profesor_calif', '')
        cursor.callproc('sendfeedback', (id_profesor, id_cliente, comentario, claridad_profesor_calif, precio_profesor_calif, disponibilidad_profesor_calif))    
        cnx.commit()
        return jsonify({
            'message': 'Feedback enviado exitosamente','status': 'success','data': data}), 201
    
    except mysql.connector.Error as err:
        print(f"Error al enviar feedback: {err}")
        return jsonify({
            'message': 'Error al enviar feedback','status': 'error','data': []}), 500
    finally:
        cursor.close()
        cnx.close()


if __name__ == '__main__':
    app.run(debug=True)