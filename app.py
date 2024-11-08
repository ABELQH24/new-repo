from flask import Flask, render_template, abort, request, redirect, url_for
import sqlite3
from models import Post, sessionLocal

#def get_db_connection():
#    conn = sqlite3.connect("midatabase.db")
#    conn.row_factory = sqlite3.Row
#    return conn

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
    sesion = sessionLocal()
    posts = sesion.query(Post).all()
    sesion.close()
    
    #for post in posts:
        #print("======>", post["id"])
        #print("======>", post["title"])
        #print("======>", post["content"])
        #print("======>", post["created"])
        #print("============================================")
    return render_template(template_name_or_list="post/posts.html")

@app.route("/post/<int:post_id>", methods=["GET"])
def get_one_posts(post_id):
    #if request.method == "GET":
    #    conn = get_db_connection()
    #    post= conn.execute("SELECT * FROM posts WHERE id = ?", (post_id,)).fetchone() # crea un lista de todas esas filas y coloca dentro de post
    #    conn.close()
    #    if post is None:
    #        abort(404)
    #    print("++++++>>>>>", post)
    return render_template(template_name_or_list="post/post.html", post = post)

@app.route("/post/create", methods=["GET", "POST"])
def create_one_posts():
    #if request.method == "POST":
    #    title = request.form["title"]
    #    content = request.form["content"]
    #    conn = get_db_connection()
    #    conn.execute("INSERT INTO posts(title, content) VALUES (?,?)",
    #                  (title.upper(), content.capitalize()),)
    #    conn.commit()
    #    conn.close()
    #    print(title)
    #    print(content)
    #    return redirect(url_for("get_all_posts"))

    #if request.method == "GET":
    return render_template("post/create.html")


@app.route("/post/edit/<int:post_id>", methods=["GET", "POST"])
def edit_one_post(post_id):
    #conn = get_db_connection()
    #post = conn.execute("SELECT * FROM posts WHERE id = ?", (post_id,)).fetchone()
    #conn.close()
    #print("+++  ANTES  >>>", post)
    
    #if request.method == "POST":
    #    title = request.form["title"]
    #    content = request.form["content"]
    #    conn = get_db_connection()
    #    conn.execute(
    #        "UPDATE posts SET title = ?, content = ? WHERE id = ?",
    #        (title.upper(), content.capitalize(), post_id)
    #        )
    #    conn.commit()
    #    conn.close()
    #    conn = get_db_connection()
    #    post = conn.execute("SELECT * FROM posts WHERE id = ?", (post_id,)).fetchone()
    #    conn.close()
    #    print("+++++++ DESPUÉS >>>>>", post)
    #    return redirect(url_for("get_all_posts"))
    
    #elif request.method == "GET":
    return render_template(template_name_or_list="post/edit.html")


@app.route("/post/delete/<int:post_id>", methods=["POST"])
def delete_one_post(post_id):
    conn = get_db_connection()
    #post = conn.execute("SELECT * FROM posts WHERE id = ?", (post_id,)).fetchone()
    
    #if post is None:
    #    abort(404)
    #if request.method == "POST":
    #    conn.execute("DELETE FROM posts WHERE id = ? ", (post_id,))
    #    conn.commit()
    #    conn.close()
    return redirect(url_for('get_all_posts'))

#Ejecutar la Aplicación
if __name__ == '__main__':
    app.run(debug=True) 