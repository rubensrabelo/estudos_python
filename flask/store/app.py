from flask import Flask


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
    return {"stores": stores}
