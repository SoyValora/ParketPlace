from flask import Flask, render_template, request, redirect, url_for
import requests
from datetime import datetime


app = Flask(__name__)


# Ruta de login
@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        usuario = request.form["usuario"]
        contrasena = request.form["contrasena"]
        
        # Simulación de usuario y contraseña correctos
        if usuario == "admin" and contrasena == "1234":
            return redirect(url_for("dashboard"))
        else:
            return render_template("index.html", error="Usuario o contraseña incorrectos")
    return render_template("index.html")

# Página del dashboard
@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")

# Ruta para registrar usuario
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # Capturamos los datos del formulario
        nombres = request.form["nombres"]
        apellidos = request.form["apellidos"]
        documentoIdent = request.form["documentoIdent"]
        codUniversidad = request.form["codUniversidad"]
        email = request.form["email"]
        password = request.form["password"]
        programa = request.form["programa"]
        fechaNacimiento = request.form["fechaNacimiento"]
        celular = request.form["celular"]

        # Convertir fecha a string si necesitas (NestJS espera string tipo '2024-04-25')
        fechaNacimiento = datetime.strptime(fechaNacimiento, '%Y-%m-%d').isoformat() + "Z"

         # Convertir codUniversidad a int
        try:
            codUniversidad = int(codUniversidad)
        except ValueError:
            return render_template("register.html", mensaje="El código de universidad debe ser un número entero.")

        # Crear el payload
        payload = {
            "nombres": nombres,
            "apellidos": apellidos,
            "documentoIdent": documentoIdent,
            "codUniversidad": codUniversidad,
            "email": email,
            "password": password,
            "programa": programa,
            "fechaNacimiento": fechaNacimiento,
            "celular": celular
        }

        try:
            # Enviar POST a NestJS
            response = requests.post("http://localhost:3000/usuario/registro", json=payload)

            if response.status_code == 201 or response.status_code == 200:
                mensaje = "Usuario registrado exitosamente en el backend"
            else:
                mensaje = f"Error al registrar usuario: {response.text}"
        except Exception as e:
            mensaje = f"Error de conexión: {str(e)}"

        return render_template("register.html", mensaje=mensaje)

    return render_template("register.html")

@app.route('/recargar_carnet')
def recargar_carnet():
    return render_template('recargar_carnet.html')

# Iniciar la aplicación Flask
if __name__ == "__main__":
    app.run(debug=True)
