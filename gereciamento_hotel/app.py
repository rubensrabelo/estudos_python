from flask import Flask
from flask_restful import Resource, Api


app = Flask(__name__)
api = Api(app)


class Hoteis(Resource):
    def get(self):
        return {"Hoteis": "Meus hoteis"}


api.add_resource(Hoteis, "/hoteis")

if __name__ == "__main__":
    # http://127.0.0.1:5000/hoteis
    app.run(debug=True)
