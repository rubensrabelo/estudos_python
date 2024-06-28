from flask import Flask, request


app = Flask(__name__)

stores = [{
    "name": "My Store",
    "items": [{
        "name": "My Item",
        "price": 15.99
    }]
}]


@app.get("/stores")
def get():
    return {"stores": stores}, 200


@app.get("/store/<string:name>")
def get_one_store(name):
    for store in stores:
        if store["name"] == name:
            return store, 200
    return {"message": "Store not found."}, 404


@app.post("/stores")
def post():
    store_data = request.get_json()
    new_store = {"name": store_data["name"], "items": []}
    stores.append(new_store)
    return new_store, 201


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
