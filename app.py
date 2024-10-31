from flask import Flask, render_template

#Crear la Aplicación
app = Flask(__name__)

#Crear la Ruta Principal
@app.route("/", methods=["GET"])
def base():
    context = {"name":"jorge"}
    return render_template(template_name_or_list="base.html", context=context)

@app.route("/Home", methods=["GET"])
def home():
    return render_template("home.html"
#Ejecutar la Aplicación
if __name__ == '__main__':
    app.run(debug=True)