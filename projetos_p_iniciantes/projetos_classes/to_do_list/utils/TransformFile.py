import json


class JSONFile:
    @staticmethod
    def save_in_json(dictionary: dict) -> None:
        json_string = json.dumps(dictionary, indent=4)
        with open("db.json", "a") as file:
            file.write(json_string)

    @staticmethod
    def open_json() -> dict:
        with open("db.json", "r") as file:
            json_file = file.read()
            dict_file = json.loads(json_file)
            return dict_file
