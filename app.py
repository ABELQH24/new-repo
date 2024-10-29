from flask import Flask, render_template

#Crear la Aplicación
app = Flask(__name__)

#Crear la Ruta Principal
@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

#Ejecutar la Aplicación
if __name__ == '__main__':
    app.run(debug=True)