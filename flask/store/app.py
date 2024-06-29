import uuid
from flask import Flask, request

from db import stores, items


app = Flask(__name__)



@app.get("/stores")
def get():
    return {"stores": list(stores.values)}, 200


@app.get("/store/<string:store_id>")
def get_one_store(store_id):
    try:
        return stores[store_id], 200
    except IndexError:
        return {"message": "Store not found."}, 404


@app.post("/stores")  # Parei aqui
def post():
    store_data = request.get_json()
    store_id = uuid.uuid4().hex
    store = {**store_data, id: store_id}
    stores[store_id] = store
    return store, 201


@app.get("/store/<string:name>/item")
def get_items(name):
    for store in stores:
        if store["name"] == name:
            return {"items": store["items"]}, 200
    return {"message": "Store not found."}, 404


@app.post("/stores/<string:name>/item")
def post_item_in_store(name):
    for store in stores:
        if store["name"] == name:
            item_data = request.get_json()
            new_item = {**item_data}
            store["items"].append(new_item)
            return new_item, 201
    return {"message": "Store not found."}, 404
