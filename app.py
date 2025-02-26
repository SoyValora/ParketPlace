from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Ruta principal con formulario de inicio de sesión
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

# Página después del login
@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")

if __name__ == "__main__":
    app.run(debug=True)
