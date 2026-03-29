import json

FILE_PATH = "/storage/emulated/0/expences.json"

def load_data():
    try:
        with open(FILE_PATH, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []

def save_data(expences):
    with open(FILE_PATH, "w") as file:
        json.dump(expences, file, indent=4)