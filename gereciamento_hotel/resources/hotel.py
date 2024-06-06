from flask_restful import Resource, reqparse

from models.hotel import HotelModel


hoteis = [
    {
        "hotel_id": "alpha",
        "nome": "Alpha Hotel",
        "estrelas": 4.3,
        "diaria": 420.34,
        "cidade": "RJ"
    },
    {
        "hotel_id": "bravo",
        "nome": "Bravo Hotel",
        "estrelas": 4.4,
        "diaria": 380.90,
        "cidade": "SC"
    },
    {
        "hotel_id": "charlie",
        "nome": "Charlie Hotel",
        "estrelas": 3.90,
        "diaria": 320.20,
        "cidade": "SC"
    },
]


class Hoteis(Resource):
    def get(self):
        return {"Hoteis": hoteis}


class Hotel(Resource):
    argumentos = reqparse.RequestParser()
    argumentos.add_argument("nome")
    argumentos.add_argument("estrelas")
    argumentos.add_argument("diaria")
    argumentos.add_argument("cidade")

    def find_hotel(hotel_id):
        for hotel in hoteis:
            if hotel["hotel_id"] == hotel_id:
                return hotel
        return None

    def get(self, hotel_id):
        hotel = Hotel.find_hotel(hotel_id)
        if hotel:
            return hotel
        return {"message": "Hotel no found."}, 404

    def post(self, hotel_id):
        dados = Hotel.argumentos.parse_args()

        hotel_objeto = HotelModel(hotel_id, **dados)
        novo_hotel = hotel_objeto.json()

        hoteis.append(novo_hotel)

        return novo_hotel, 200

    def put(self, hotel_id):
        dados = Hotel.argumentos.parse_args()
        hotel = Hotel.find_hotel(hotel_id)

        hotel_objeto = HotelModel(hotel_id, **dados)
        novo_hotel = hotel_objeto.json()

        if hotel:
            hotel.update(novo_hotel)
            return novo_hotel, 200

        hoteis.append(novo_hotel)
        return novo_hotel, 201

    def delete(self, hotel_id):
        global hoteis
        hoteis = [hotel for hotel in hoteis if hotel["hotel_id"] != hotel_id]
        return {"message": "hotel deleted."}
