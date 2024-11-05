from flask import Flask, render_template

#Crear la Aplicación
app = Flask(__name__)

#Crear la Ruta Principal
@app.route("/", methods=["GET"])
def base():
    context = {
        "name":"BASE",
        "project":"web developer Flask"
        }
    return render_template(template_name_or_list="base.html", **context)

@app.route("/home", methods=["GET"])
def home():
    context = {
        "name_home":"Home",
        "my_name": "Jorge"
        }
    return render_template(template_name_or_list="home.html", **context)
#Ejecutar la Aplicación
if __name__ == '__main__':
    app.run(debug=True) 