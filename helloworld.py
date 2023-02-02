from flask import Flask
import requests

app = Flask(__name__)


@app.route("/")
def hello():
    url = "https://pokeapi.co/api/v2/pokemon/eevee"
    response = requests.get(url).json()
    moves = response["moves"]
    pokemonName = response["name"]
    result = ""

    for move in moves:
        result = result + " " + move["move"]["name"] + ","

    result = result.rstrip(",")

    return f"{pokemonName} has {len(moves)} moves. They are: {result}"
