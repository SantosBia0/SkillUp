from flask import Flask, render_template, request, redirect, url_for
import mysql.connector
import os

app = Flask(__name__)

# Configuração segura para Nuvem ou Local
def get_db_connection():
    return mysql.connector.connect(
        host=os.environ.get("DB_HOST", "localhost"),
        user=os.environ.get("DB_USER", "root"),
        password=os.environ.get("DB_PASSWORD", "alunolab"),
        database=os.environ.get("DB_NAME", "saep"),
        port=int(os.environ.get("DB_PORT", 3306))
    )

@app.route("/")
def login():
    return render_template("index.html") 

@app.route("/inicio")
def inicio():
    return render_template("inicio.html")

@app.route("/test-static")
def test_static():
    import os
    static_path = os.path.join(app.root_path, 'static', 'css', 'style.css')
    return f"CSS exists: {os.path.exists(static_path)}<br>Path: {static_path}"

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
            
            # Verifica se já existe
            cursor.execute("SELECT * FROM usuarios WHERE email=%s OR usuario=%s", (email, usuario))
            if cursor.fetchone():
                return "Email ou usuário já cadastrado!"
            
            # Insere novo usuário
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

    return render_template("index.html") # Ou sua tela de cadastro separada

if __name__ == "__main__":
    app.run(debug=True)