
from flask import Flask, render_template, request, redirect, url_for, flash
from flask import Flask, render_template, request, redirect, url_for
import requests
from datetime import datetime
from flask import session


app = Flask(__name__)
app.secret_key = 'clave_secreta_segura'

from flask import Flask, render_template, request, redirect, url_for, session
import requests

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("usuario")
        password = request.form.get("contrasena")

        payload = {
            "email": email,
            "password": password
        }

        try:
            response = requests.post("http://localhost:3000/usuario/ingreso", json=payload)
            print("Status code:", response.status_code)

            if response.status_code in [200, 201]:
                data = response.json()
                print("Respuesta del backend:", data)

                if "access_token" in data:
                    session["token"] = data["access_token"]
                    session["usuario"] = data["usuario"]["email"]
                    session["nombre"] = data["usuario"]["nombres"]
                    return redirect(url_for("dashboard"))
                else:
                    return render_template("index.html", error="Error: no se recibió el token")

            else:
                print("Error al iniciar sesión:", response.text)
                return render_template("index.html", error="Usuario o contraseña incorrectos")

        except Exception as e:
            print("Excepción en login:", e)
            return render_template("index.html", error="Error de conexión con el servidor")

    return render_template("index.html")

@app.route("/logout")
def logout():
    session.clear()  # Esto elimina todos los datos de sesión
    return redirect(url_for("login"))  # Redirige al login

# Página del dashboard
@app.route("/dashboard")
def dashboard():
    if "usuario" not in session:
        return redirect(url_for("login"))
    return render_template("dashboard.html", usuario=session["nombre"], email=session["usuario"])

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

@app.route('/visitor_register', methods=['GET'])
def visitantes():
    return render_template('visitantes.html')

# Ruta para procesar los datos del formulario
@app.route('/visitor_register', methods=['POST'])
def visitor_register():
    # Obtener los datos del formulario
    placa = request.form.get('placa')
    nombre = request.form.get('nombre')
    apellido = request.form.get('apellido')
    valor = request.form.get('valor')  # Este es el valor a pagar con formato, sin el signo de pesos
    pago = request.form.get('pago')  # El tipo de pago seleccionado

    # Validar datos básicos
    if not placa or not nombre or not apellido or not valor or not pago:
        flash('Todos los campos son obligatorios.')
        return redirect(url_for('visitantes'))

    # Procesar los datos, por ejemplo, puedes guardar en la base de datos o realizar otras acciones
    print(f"Placa: {placa}, Nombre: {nombre}, Apellido: {apellido}, Valor a Pagar: {valor}, Método de Pago: {pago}")

    # Aquí podrías agregar lógica para guardar en la base de datos si lo necesitas.
    
    # Redirigir a una página de éxito o a la misma página
    flash('Pago Procesado exitosamente.')
    return redirect(url_for('visitantes'))  # O redirigir a una página de éxito

# Iniciar la aplicación Flask
if __name__ == "__main__":
    app.run(debug=True)
