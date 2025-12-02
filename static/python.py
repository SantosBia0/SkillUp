# IMPORTANDO AS BIBLIOTECAS
from flask import Flask, render_template, request, redirect, url_for
import mysql.connector

# INICIAR MEU APP
app = Flask(__name__)

# CONEXAO COM O BANCO
def get_db_connection():
    return mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "alunolab",
        database = "saep",
        port = 3303
    )
# CHAMANDO A CONEXAO PARA A VARIAVEL con
con = get_db_connection()
# JOGANDO A CONEXAO PARA A VARIAVEL cursor
cursor = con.cursor()
nome = "Beatriz"
email = "beatriz@gmail.com"
usuario = "Admin"
senha = "Admin123"
tipo = "admin"
# PESQUISANDO NO BANCO DE DADOS SE JA TEM O EMAIL CADASTRADO
cursor.execute("SELECT * FROM usuarios WHERE email=%s", (email,))

# PRGUNTAR SE ENCONTROU ALGUEM CADASTRADO
if cursor.fetchone() is None:
    sql = "INSERT INTO usuarios (nome, email, usuario, senha, tipo) VALUES (%s, %s, %s, %s, %s)"
    valores = (nome, email, usuario, senha, tipo)
    cursor.execute(sql, valores)
    con.commit()

cursor.close()
con.close()

@app.route("/")
def login():
    return render_template("login.html")

@app.route("/cadastrar", methods=["GET","POST"])
def cadastrar():
    # PEGANDO INFORMACOES DO FORMULARIO
    if request.method == "POST":
        nome = request.form.get("nome")
        email = request.form.get("email")
        usuario = request.form.get("usuario")
        senha = request.form.get("senha")
        tipo = request.form.get("tipo") or "user"

        # VERIFICANDO SE FOI PREENCHIDO
        if not nome or not email or not usuario or not senha:
            return "Preencha todos os campos!"
        # CHAMANDO A CONEXAO
        con = get_db_connection()
        cursor = con.cursor()
        # EXECUTANDO O SELECT
        cursor.execute("SELECT * FROM usuarios WHERE email=%s or usuario=%s", (email, usuario))

        # EXECUTANDO O SELECT PARA VERIFICAR SE EMAIL OU USUARIO JA EXISTEM
        if cursor.fetchone():
            cursor.close()
            con.close()
            return "Email ou usuário já cadastrado!"
            # INSTRUCAO DE INSERCAO NO BANCO
        sql = "INSERT INTO usuarios (nome, email, usuario, senha, tipo) VALUES (%s, %s, %s, %s, %s)"
        valores = (nome, email, usuario,senha, tipo)
        cursor.execute(sql, valores)
        con.commit()

        # RETORNO SE ESTIVER OK
        return "Usuário cadastrado com sucesso!"
        return redirect(url_for("login"))

    return render_template("cadastrar.html")

# FINALIZAR MEU APP
if __name__ == "__main__":
    app.run(debug=True)