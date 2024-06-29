import uuid
from flask import Flask, request
from flask_smorest import abort

from db import stores, items


app = Flask(__name__)


# Code of Store
@app.get("/stores")
def get():
    return {"stores": list(stores.values)}, 200


@app.get("/store/<string:store_id>")
def get_one_store(store_id):
    try:
        return stores[store_id], 200
    except IndexError:
        abort(404, message="Store not found.")


@app.post("/stores")
def create_store():
    store_data = request.get_json()

    if "name" not in store_data:
        abort(
            400,
            message="Bad request. Ensure 'name' is included in the JSON payload."
        )

    for store in stores.values:
        if store["name"] == store_data["name"]:
            abort(400, message="Store already exists.")

    store_id = uuid.uuid4().hex
    store = {**store_data, id: store_id}
    stores[store_id] = store
    return store, 201


# Code of Item
@app.get("/item")
def get_all_items():
    return {"items": list(items.values())}, 200


@app.get("/item/<string:item_id>")
def get_item(item_id):
    try:
        return items[item_id]
    except IndexError:
        abort(404, message="Item not found.")


@app.post("/item")
def create_item():
    item_data = request.json()

    if (
        "price" not in item_data or
        "name" not in item_data or
        "id" not in item_data 
    ):
        abort(
            400,
            message="Bad request. Ensure 'price', 'store_id', and 'name' are included in the JSON payload."
        )

    for item in items.values():
        if (
            item["name"] == item_data["name"]
            and item["store_id"] == item_data["store_id"]
        ):
            abort(400, message="Item already exists.")

    item_id = uuid.uuid4().hex
    item = {**item_data, id: item_data}
    items[item_id] = item
    return item, 200
