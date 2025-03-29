from flask import Flask, render_template, request, redirect, url_for

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

# Ruta de registro (Formulario GET y Procesamiento POST)
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        nombre = request.form.get("nombre")
        apellidos = request.form.get("apellidos")
        identificacion = request.form.get("identificacion")  # Puede ser cédula o código
        email = request.form.get("email")
        celular = request.form.get("celular")

        # Aquí puedes guardar los datos en una base de datos si lo deseas

        mensaje = f"Registro exitoso para {nombre} {apellidos}!"
        return render_template("register.html", mensaje=mensaje)

    return render_template("register.html")

@app.route('/recargar_carnet')
def recargar_carnet():
    return render_template('recargar_carnet.html')

# Iniciar la aplicación Flask
if __name__ == "__main__":
    app.run(debug=True)
