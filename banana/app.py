from flask import Flask, render_template

app = Flask(__name__)

lista_produtos = [
        {"nome": "Amendoas", "descricao": "Comum"},
        {"nome": "Queijo quente", "descricao": "Raro"},
        {"nome": "Cheesecake", "descricao": "Lendário"}
    ]

@app.route("/")
def home():
    return render_template('base.html')

@app.route("/contato")
def contato():
    return "<h1>Contato</h1>"

@app.route("/produtos")
def produtos():
    return render_template('produtos.html', produtos= lista_produtos)

@app.route("/produtos/<nome>")
def produto(nome):
    for produto in lista_produtos:
        if produto["nome"].lower() == nome.lower():
            return f"{produto ['nome']}, {produto ['descricao']}"

    return "Produto não encontrado"