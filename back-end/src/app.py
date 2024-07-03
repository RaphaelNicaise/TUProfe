from flask import Flask, jsonify, request
import mysql.connector
from mysql.connector import pooling
from config import developmentConfig
from flask_jwt_extended import JWTManager, jwt_required, create_access_token, get_jwt_identity
import bcrypt


app = Flask(__name__)
app.config.from_object(developmentConfig)
# inicializa el JWTManager con la app de Flask
jwt = JWTManager(app)

dbconfig = { # datos de la base de datos
    "database": developmentConfig.SQLConfig.DATABASE,
    "user":developmentConfig.SQLConfig.USER,
    "password": developmentConfig.SQLConfig.PASSWORD,
    "host": developmentConfig.SQLConfig.HOST,
    "port": developmentConfig.SQLConfig.PORT,
}
# cree un pool de conexiones, con un maximo de 5 conexiones, que se van reutilizando
# evitando tener que crear y cerrar conexiones cada vez que se hace una peticion
cnxpool = mysql.connector.pooling.MySQLConnectionPool(pool_name="mypool", pool_size=5, **dbconfig)
# funcion para obtener una conexion del pool
def get_connection():
    try:
        return cnxpool.get_connection()                                       
    except mysql.connector.Error as err:
        print(f"{err}")
        return None

# RUTAS DE LA API
@app.route('/')
def rutas_menu():
    
    return jsonify({
        'message': 'Bienvenido a la API de la Universidad, la api esta funcionando correctamente',
        'status': 'success',
        'data': {
            'rutas': [
                '/api/data/materias', # GET Y POST
                '/api/data/materias/<id_materia>', # GET
                '/api/data/clientes', # GET Y POST
                '/api/data/clientes/<id_cliente>',
                '/api/data/profesores', # GET
                '/api/data/profesores/<id_profesor>', # GET
                '/api/data/sendfeedback' # POST
                '/api/data/info_profesores' # GET
            ]
        }
    })
# Get de todas las materias y su informacion
@app.route('/api/data/materias', methods=['GET'])
def get_materias():
    try:
        # Se crea conexion y cursor
        cnx = get_connection()
        cursor = cnx.cursor(dictionary=True) # Lo que se devuelva, se transformara a un diccionario
        cursor.execute("select * from materias") # Ejecuta la query
        resultados = cursor.fetchall() # Guarda la query en una variable como un diccionario
    except mysql.connector.Error as err: # Cualquier error de SQL se mostrara en la terminal
        print(f"{err}")
    finally: # Se cierra el cursor y la conexion
        cursor.close()
        cnx.close()
        if resultados: # Si existen resultados, se devuelven, si no, se devuelve un error 404 (no encontrado)
            data = {
                'message': 'get de todas las materias','status': 'success','data': resultados} 
            return jsonify(data)
        else:
            return jsonify({
                'message': 'No se encontraron las materias', 'status': 'error','data': []}), 404
            

# Get de una materia especifica
@app.route('/api/data/materias/<id_materia>', methods=['GET'])
def get_materia(id_materia):
    
    try:
        cnx = get_connection()
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
        
# Get de todos los clientes

@app.route('/api/data/clientes', methods=['GET'])
def clientes():
    if request.method == 'GET':
        try:  
            cnx = get_connection()
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
                
# Get para obtener un cliente especifico            
@app.route('/api/data/clientes/<id_cliente>', methods=['GET'])
def get_cliente(id_cliente):
    try:
        cnx = get_connection()
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

# Get de todos los profesores
@app.route('/api/data/profesores', methods=['GET'])
def get_profesores():
    try:
        cnx = get_connection()
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
                'data': resultados}
            return jsonify(data)
        else:
            return jsonify({
                'message': 'No se encontraron profesores','status': 'error','data': []}), 404

# Get de un profesor especifico
@app.route('/api/data/profesores/<id_profesor>', methods=['GET'])
def get_profesor(id_profesor):
    try:
        cnx = get_connection()
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


# endpoint para enviar feedback a un profesor, mediante un cliente. POST
@app.route('/api/data/sendfeedback', methods=['POST'])
def sendfeedback():
    try:
        cnx = get_connection()
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
        disponibilidad_profesor_calif = data.get('disponibilidad_profesor_calif', '') # el procedimiento recibe estos datos, y despues calcula la califiacion general, y lo inserta
        cursor.callproc('sendfeedback', (id_profesor, id_cliente, comentario, claridad_profesor_calif, precio_profesor_calif, disponibilidad_profesor_calif))    
        cnx.commit()
        return jsonify({
            'message': 'Feedback enviado exitosamente','status': 'success','data': data}), 201
    # Las validaciones se manejan en MySQL, por lo que no se manejan en el codigo
    # Cualquier error se mostrara en la terminal, y devolvera error en e JSOB
    except mysql.connector.Error as err:
        print(f"Error al enviar feedback: {err}")
        return jsonify({
            'message': 'Error al enviar feedback','status': 'error','data': []}), 500
    finally:
        cursor.close()
        cnx.close()

# Get de la informacion de todos los profesores, con la materia que dan
@app.route('/api/data/info_profesores', methods=['GET'])
def get_info_profesores():
    try:
        cnx = get_connection()
        cursor = cnx.cursor(dictionary=True)
        cursor.execute('select * from info_profesores')
        resultados = cursor.fetchall()
    except mysql.connector.Error as err:
        print(f"{err}")
    finally:
        cursor.close()
        cnx.close()
        if resultados:
            data = {
                'message': 'Get de la informacion de todos los profesores',
                'status': 'success',
                'data': resultados}
            return jsonify(data)
        else:
            return jsonify({
                'message': 'No se encontraron profesores','status': 'error','data': []}), 404


@app.route('/api/register', methods=['POST'])
def register():
    try:
            cnx = get_connection()
            cursor = cnx.cursor(dictionary=True)
            if request.headers['Content-Type'] != 'application/json': # CHEQUEA QUE EL CONTENT TYPE SEA JSON
                return jsonify({
                'message': 'Tipo de contenido no soportado. Asegúrate de enviar JSON.','status': 'error'}), 415
            data = request.json # RECOLECTA LOS DATOS DEL JSON, Y LOS GUARDA EN VARIABLES
            nombre = data.get('nombre', '')
            apellido = data.get('apellido', '')
            correo = data.get('correo', '')
            password = data.get('password', '') # Obtenemos la password ingresada por el usuario
            # y despues la hasheamos con bcrypt
            password_hasheada = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
            telefono = data.get('telefono', '')
            descripcion = data.get('descripcion', '')  
            # LLAMA AL PROCEDIMIENTO INSERT_CLIENTE, Y LE PASA LOS DATOS
            cursor.callproc('insert_cliente', (nombre, apellido, correo,password_hasheada, telefono, descripcion)) 
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

#@app.route('/api/login', methods=['POST'])# Ruta para el login

@app.route('/protected', methods=['GET'])
@jwt_required()
def protected():
    current_user = get_jwt_identity()
    return jsonify(logged_in_as=current_user), 200

# Ejectuar la aplicacion mediante python src/app.py si estas parado en back-end
if __name__ == '__main__':
    app.run(debug=True)