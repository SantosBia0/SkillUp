from flask import Flask, render_template, request, redirect, url_for
import mysql.connector
import os

app = Flask(__name__, static_folder="static", template_folder="templates")

def get_db_connection():
    return mysql.connector.connect(
    host=os.environ["DB_HOST"],
    user=os.environ["DB_USER"],
    password=os.environ["DB_PASSWORD"],
    database=os.environ["DB_NAME"],
    port=int(os.environ["DB_PORT"]),
    ssl_disabled=False
)

@app.route("/")
def login():
    return render_template("index.html") 

@app.route("/inicio")
def inicio():
    return render_template("inicio.html")

@app.route("/cadastrar", methods=["GET","POST"])
def cadastrar():
    if request.method == "POST":
        nome = request.form.get("nome")
        email = request.form.get("email")
        usuario = request.form.get("usuario")
        senha = request.form.get("senha")
        tipo = "user"

        if not nome or not email or not usuario or not senha:
            return "Preencha todos os campos!"
        
        try:
            con = get_db_connection()
            cursor = con.cursor()
            
            cursor.execute("SELECT * FROM usuarios WHERE email=%s OR usuario=%s", (email, usuario))
            if cursor.fetchone():
                return "Email ou usuário já cadastrado!"
            
            sql = "INSERT INTO usuarios (nome, email, usuario, senha, tipo) VALUES (%s, %s, %s, %s, %s)"
            cursor.execute(sql, (nome, email, usuario, senha, tipo))
            con.commit()
            return "Usuário cadastrado com sucesso!"
        except Exception as e:
            return f"Erro no banco de dados: {e}"
        finally:
            if 'con' in locals() and con.is_connected():
                cursor.close()
                con.close()

    return render_template("index.html")
