from flask import Flask, jsonify, request
import db

# (webservice) API SOAP: Simple Object Access Protocol
# API Rest: REpresentational State Transfer
# JSON: JavaScript Object Notation

## app = Flask(__name__)
app = Flask("API de Carros") ## -> dando um nome para essa API

# area para a criação das funções
@app.route("/hello", methods=["GET"]) ## -> definindo URL e método para chamar a função
def get_hello():
    resp = {
        "msg": "Hello, World!"
    }
    ## sempre vamos devolver uma tupla
    return (jsonify(resp), 200) ## 200 -> representa o HttpStatusCode OK (funcionou)

@app.route("/carros", methods=["GET"])
def get_all_cars():
    return (jsonify(db.carros), 200)

app.run(debug=True) ## -> colocando o serviço no ar