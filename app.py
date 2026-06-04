from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")

def inicio():
    nombre_profesor = "Henry Ortegon"
    email_profesor = "henry@kyrbot.com"
    horario = "Miercoles 16:45-18:10 | Jueves 12:30-14:20"
    aula = "215"
    descripcion = "Aprenderemos Python, Flask y construiremos un portal web real"

    return render_template(
    "index.html",
    profesor=nombre_profesor,
    horario=horario
)

@app.route("/informacion")
def informacion():
datos = {
"aula": "215",
"profesor": "Henry Ortegon",
"horario": "Miercoles 16:45-18:10 | Jueves 12:30-14:20"
}

return render_template("info.html", **datos)

@app.route("/recursos")
def recursos():
return render_template("recursos.html")

@app.route("/tareas")
def tareas():
return render_template("tareas.html")

if __name__ == "main":
    app.run(debug=True)