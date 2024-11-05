from flask import Flask, render_template
import sqlite3

def get_db_connection():
    conn = sqlite3.connect("midatabase.db")
    conn.row_factory = sqlite3.Row
    return conn

#Crear la Aplicación
app = Flask(__name__)

#Crear la Ruta Principal -> "CONTROLADOR"-> va tener la función con conectar con la base de datos
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

@app.route("/post", methods=["GET"])
def get_all_posts():
    conn = get_db_connection()
    posts= conn.execute("SELECT * FROM posts").fetchall() # crea un lista de todas esas filas y coloca dentro de post
    conn.close()
    for post in posts:
        print("======>", post["id"])
        print("======>", post["title"])
        print("======>", post["content"])
        print("======>", post["created"])
        print("============================================")

    return render_template(template_name_or_list="posts.html")

#Ejecutar la Aplicación
if __name__ == '__main__':
    app.run(debug=True) 