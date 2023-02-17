from flask import Flask, jsonify, make_response
import requests

app = Flask(__name__)


@app.route("/<pokemon>")
def getPokemon(pokemon):
    pokeAPI = f"https://pokeapi.co/api/v2/pokemon-form/{pokemon}"
    pokeAPIResponse = ""

    try:
        pokeAPIResponse = requests.get(pokeAPI).json()
    except BaseException as be:
        error = {
            "code": 100,
            "description": str(be.args[0])
        }
        return jsonify(error)
    
    sprites = pokeAPIResponse["sprites"]
    frontImage = sprites["front_default"]
    response = make_response({
        "name": f"{pokemon}",
        "image": frontImage
    })
    response.headers['Access-Control-Allow-Origin'] = '*'

    return response
    

