from flask import Flask

# Crear la app Flask
app = Flask(__name__)

# Ruta principal para verificar que funciona
@app.route('/')
def home():
    return '¡Hola, esta es mi app Flask funcionando!'

# Ejecutar el servidor
if __name__ == '__main__':
    app.run(debug=True)