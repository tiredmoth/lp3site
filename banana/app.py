from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

lista_produtos = [
        {"nome": "Amendoas", "descricao": "eca", "preco": "23 reais", "imagem": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQZPMS_bny0MEJXjIiCB6FjD6k9U8XGd9IGxw&s"},
        {"nome": "Queijo quente", "descricao": "gostoso", "preco": "5 reais", "imagem": "https://img.estadao.com.br/resources/jpg/7/3/1543522402137.jpg"},
        {"nome": "Gwimbly gun", "descricao": "Se eu tivesse uma comigo agora...", "preco": "50 reais", "imagem": "https://images.voicy.network/Content/Clips/Images/e84b4454-dac2-46ca-9ee0-67ffb0ac4d61-small.png"}
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
            return f"{produto ['nome']}, {produto ['descricao']}, {produto ['preco']}, {produto ['imagem']}"

    return "Produto não encontrado"

@app.route("/produtos/cadastro")
def cadastro_produto():
    return render_template("cadastro-produto.html")

@app.route("/produtos", methods=['POST'])
def salvar_produto():
    nome = request .form['nome']
    descricao = request.form['descricao']
    produto = {"nome": nome, "descricao": descricao, "preco": preco, "imagem": imagem}
    lista_produtos.append(produto)
    return redirect(url_for("produtos"))

app.run(port=5001)