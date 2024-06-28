from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Proyecto corriendo el entorno virtual'

@app.route('/saludo')
def saludo():
    return '¡Hola! Este es un saludo desde la ruta /saludo.'

if __name__ == '__main__':
    app.run(debug=True)

