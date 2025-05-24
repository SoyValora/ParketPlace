from flask import Flask, render_template, request, redirect, url_for, flash

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
