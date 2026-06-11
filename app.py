from flask import Flask, render_template, request, redirect, url_for, session
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = "clave-secreta-1114"

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///portal.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    usuario = db.Column(db.String(50), unique=True, nullable=False)
    contraseña = db.Column(db.String(200), nullable=False)
    rol = db.Column(db.String(20), nullable=False)

    def establecer_contraseña(self, contraseña):
        self.contraseña = generate_password_hash(contraseña)

    def verificar_contraseña(self, contraseña):
        return check_password_hash(self.contraseña, contraseña)


class Estudiante(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    programa = db.Column(db.String(50), nullable=False)
    fecha_inscripcion = db.Column(db.DateTime, default=db.func.now())


class Tarea(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(100), nullable=False)
    descripcion = db.Column(db.Text, nullable=False)
    fecha_entrega = db.Column(db.String(50), nullable=False)

# CORRECCIÓN: Se sacó la función fuera de la clase Tarea y se eliminó la duplicada
@app.route("/login", methods=["GET", "POST"])
def login():
    mensaje = None

    if request.method == "POST":
        usuario = request.form.get("usuario")
        contraseña = request.form.get("contraseña")

        user = Usuario.query.filter_by(usuario=usuario).first()

        if user and user.verificar_contraseña(contraseña):
            session["usuario_id"] = user.id
            session["usuario_nombre"] = user.usuario
            session["rol"] = user.rol

            if user.rol == "profesor":
                return redirect(url_for("panel_profesor"))

            return redirect(url_for("panel_estudiante"))

        mensaje = "Usuario o contraseña incorrectos"

    return render_template("login.html", mensaje=mensaje)


@app.route("/")

def inicio():
    
    return render_template(
        "index.html",
        profesor="Henry Ortegon",
        email="henry@kyrbot.com",
        horario="Miercoles 16:45-18:10 | Jueves 12:30-14:20",
        aula="215",
        descripcion="Aprenderemos Python, Flask y construiremos un portal web real"
    )

@app.route("/informacion")
def informacion():
    objetivos = [
         "Aprender Python", 
         "Aprender Flask", 
         "Crear aplicaciones web" 
    ]
    return render_template(
        "informacion.html",
        profesor="Henry Ortegon",
        aula="215",
        horario="Miercoles 16:45-18:10 | Jueves 12:30-14:20",
        objetivos=objetivos
    )

@app.route("/recursos")
def recursos():
    enlaces = [
        {"nombre": "Documentacion Flask", "url": "https://flask.palletsprojects.com"},
        {"nombre": "Tutorial Python", "url": "https://docs.python.org"},
        {"nombre": "GitHub del Profesor", "url": "https://github.com/hortegon"},
        {"nombre": "MDN - HTML y CSS", "url": "https://developer.mozilla.org"}
    ]
    return render_template(
        "recursos.html",
        enlaces=enlaces
    )

@app.route("/tareas")
def tareas():
    lista_tareas = [
        {"numero": 1, "titulo": "Portal Base", "fecha": "25/05/2026"},
        {"numero": 2, "titulo": "Datos Dinamicos", "fecha": "30/05/2026"},
        {"numero": 3, "titulo": "Multiples Paginas", "fecha": "05/06/2026"}
    ]
    return render_template(
        "tareas.html",
        tareas=lista_tareas
    )

@app.route("/inscripcion", methods=["GET", "POST"])
def inscripcion():
    mensaje = None

    if request.method == "POST":
        nombre = request.form.get("nombre")
        email = request.form.get("email")
        programa = request.form.get("programa")

        if nombre and email and programa:

            try:
                nuevo_estudiante = Estudiante(
                    nombre=nombre,
                    email=email,
                    programa=programa
                )

                db.session.add(nuevo_estudiante)
                db.session.commit()

                mensaje = f"Bienvenido {nombre}! Te hemos registrado."

            except:
                db.session.rollback()
                mensaje = "Ese correo ya está registrado."

        else:
            mensaje = "Por favor completa todos los campos."

    return render_template(
        "inscripcion.html",
        mensaje=mensaje
    )

@app.route("/estudiantes")
def estudiantes():
    if "rol" not in session or session["rol"] != "profesor":
        return redirect(url_for("login"))

    lista_estudiantes = Estudiante.query.all()

    return render_template("estudiantes.html", estudiantes=lista_estudiantes)

    
@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("inicio"))


@app.route("/panel-profesor")
def panel_profesor():
    if "rol" not in session or session["rol"] != "profesor":
        return redirect(url_for("login"))

    return render_template(
        "panel_profesor.html",
        usuario=session["usuario_nombre"]
    )


@app.route("/panel-estudiante")
def panel_estudiante():
    if "rol" not in session:
        return redirect(url_for("login"))

    tareas = Tarea.query.all()

    return render_template(
        "panel_estudiante.html",
        usuario=session["usuario_nombre"],
        tareas=tareas
    )

@app.route("/crear-tarea", methods=["GET", "POST"])
def crear_tarea():
    if "rol" not in session or session["rol"] != "profesor":
        return redirect(url_for("login"))

    if request.method == "POST":
        nueva_tarea = Tarea(
            titulo=request.form.get("titulo"),
            descripcion=request.form.get("descripcion"),
            fecha_entrega=request.form.get("fecha_entrega")
        )

        db.session.add(nueva_tarea)
        db.session.commit()

        return redirect(url_for("mis_tareas"))

    return render_template("crear_tarea.html")


@app.route("/mis-tareas")
def mis_tareas():
    if "rol" not in session or session["rol"] != "profesor":
        return redirect(url_for("login"))

    tareas = Tarea.query.all()

    return render_template(
        "mis_tareas.html",
        tareas=tareas
    )


@app.route("/editar-tarea/<int:id>", methods=["GET", "POST"])
def editar_tarea(id):
    if "rol" not in session or session["rol"] != "profesor":
        return redirect(url_for("login"))

    tarea = Tarea.query.get_or_404(id)

    if request.method == "POST":
        tarea.titulo = request.form.get("titulo")
        tarea.descripcion = request.form.get("descripcion")
        tarea.fecha_entrega = request.form.get("fecha_entrega")

        db.session.commit()

        return redirect(url_for("mis_tareas"))

    return render_template(
        "editar_tarea.html",
        tarea=tarea
    )


@app.route("/eliminar-tarea/<int:id>")
def eliminar_tarea(id):
    if "rol" not in session or session["rol"] != "profesor":
        return redirect(url_for("login"))

    tarea = Tarea.query.get_or_404(id)

    db.session.delete(tarea)
    db.session.commit()

    return redirect(url_for("mis_tareas"))

if __name__ == "__main__":
    app.run(debug=True)
