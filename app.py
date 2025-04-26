from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import uuid 

app = Flask(__name__)

# Configuración de la base de datos (ajustar con tus credenciales)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:admin@localhost/parketplace'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Modelo de la tabla 'usuarios' en MySQL
class Usuario(db.Model):
    __tablename__ = 'usuario'  # Nombre de la tabla en MySQL

    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    nombres = db.Column(db.String(100))
    apellidos = db.Column(db.String(100))
    documentoIdent = db.Column(db.String(20))
    codUniversidad = db.Column(db.Integer)
    email = db.Column(db.String(100))
    password = db.Column(db.String(100))
    programa = db.Column(db.String(100))
    fechaNacimiento = db.Column(db.Date)
    celular = db.Column(db.String(20))
    updatedAt = db.Column(db.DateTime, default=datetime.utcnow)

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

        # Convertimos la fecha en formato 'date' que acepta MySQL
        fechaNacimiento = datetime.strptime(fechaNacimiento, '%Y-%m-%d').date()

        usuario_existente = Usuario.query.filter_by(email=email).first()

        if usuario_existente:
            mensaje = "Este correo electrónico ya está registrado."
            return render_template("register.html", mensaje=mensaje)

        # Creamos un nuevo usuario con los datos obtenidos
        nuevo_usuario = Usuario(
            nombres=nombres,
            apellidos=apellidos,
            documentoIdent=documentoIdent,
            codUniversidad=codUniversidad,
            email=email,
            password=password,
            programa=programa,
            fechaNacimiento=fechaNacimiento,
            celular=celular
        )

        try:
            # Agregamos el nuevo usuario a la base de datos
            db.session.add(nuevo_usuario)
            db.session.commit()
            mensaje = "Usuario registrado exitosamente"
        except Exception as e:
            db.session.rollback()
            mensaje = f"Error: {str(e)}"

        return render_template("register.html", mensaje=mensaje)

    return render_template("register.html")

@app.route('/recargar_carnet')
def recargar_carnet():
    return render_template('recargar_carnet.html')

# Iniciar la aplicación Flask
if __name__ == "__main__":
    app.run(debug=True)
