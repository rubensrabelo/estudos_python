# Importando a lib responsável por criar o back end da aplicação, sendo Flask (criar um objeto flask) e request (obter os dados envidos pelo o usuário)
from flask import Flask, request

# Criação da var app que irá gerenciar todos os comandos nencessário para o correto funcionamento da aplicação
app = Flask(__name__)

# flask run --> Comando para colocar a aplicação em funcionamento em uma porta
# Criando o local de armazenamento temporário da aplicação

stores = [{
    "name": "My Store",
    "items": [{
        "name": "Chair",
        "price": 15.99
    }]
}]


# Criando o método HTTP GET para obter a informação de todas as lojas cadastradas
@app.get("/store")
def get_stores():
    return {"stores": stores}, 200


# Criando o método POST para obter o cadastrado de uma nova loja
@app.post("/store")
def create_store():
    request_data = request.get_json()  # Pegando os dados enviados
    new_store = {"name": request_data["name"], "items": []}  # Colocando no formato aceito no armazenamento
    stores.append(new_store)  # Adicionando no armazenamento
    return new_store, 201  # Enviando todas as lojas e os status de sucesso


# Criando um método para inserir valores em um nome especifícado pelo usuário
@app.post("/store/<string:name>/item")
def create_item(name):
    request_data = request.get_json()
    for store in stores:
        if store["name"] == name:
            new_item = {"name": request_data["name"], "price": request_data["price"]}
            store["items"].append(new_item)
            return new_item, 201
    return {"message": "Store not found."}, 404


# Criando um método GET para obter uma loja pelo nome
@app.get("/store/<string:name>")
def get_one_store(name):
    for store in stores:
        if store["name"] == name:
            return store, 200
    return {"message": "Store not found."}, 404


@app.get("/store/<string:name>/item")
def get_item(name):
    for store in stores:
        if store["name"] == name:
            return {"items": store["items"]}, 200
    return {"message": "Store not found."}, 404
