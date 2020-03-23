#from flask import Flask   # Importar al módulo de Flask
from flask import Flask, render_template # Importar el renderizador
app = Flask(__name__)     # Crear un aplicación. Nueva instancia con par�metro name

@app.route("/")           # Se define una ruta básica. wrap o decorador
def main():               # Función correspondiente para manejar la solicitud                                                               
 #   return "Welcome!"     # Lo único que se muestra en nuestra web
    return render_template('index.html') #Devuelve el archivo plantilla renderizado



if __name__ == "__main__":#Revis si el archivo ejecutado es el programa principal
    app.run(debug=True)   # Ejecutar la aplicación. correr el servidor

# http://localhost:5000/
    
