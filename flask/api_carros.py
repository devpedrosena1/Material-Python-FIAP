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

@app.route("/carros", methods=["GET"]) ## definir rotas faz a ligação entre a URL
def get_all_cars():                    ## e a função Python. 
    return (jsonify(db.carros), 200)

# quero definir uma url que permita recuperar apenas um carro da base
# passo o ID do carro na url e recebo o carro de volta
@app.route("/carros/<int:id>", methods=["GET"])
def get_car_by_id(id: int):
    for carro in db.carros:
        if carro['id'] == id:
            return (jsonify(carro), 200)
        
    info = {
        "msg": f"Nenhum carro com id={id} encontrado",
        "status": 404
    }
    return (jsonify(info), 404)

@app.route("/carros/montadora/<string:montadora>", methods=["GET"])
def get_car_montadora(montadora: str):
    resp = []
    for carro in db.carros:
        if carro['montadora'] == montadora:
            resp.append(carro)
    if len(resp) > 0:
        return (jsonify(resp), 200)
    else:
        info = {"msg": "Nanhum carro encontrado.", "status": 404}
        return (jsonify(info), 404)
    
## post
@app.route("/carros", methods=["POST"])
def insert_car():
    carro = request.json ## pegando o carro que sera inserido no banco
    for i in range(len(db.carros)):
        c = db.carros[i]
        if c['id'] == carro['id']:
            info = {"msg": "Já existe carro com o mesmo id.",
                    "status": 406}
            return (info, 406)
        
    db.carros.append(carro)
    return (jsonify(carro), 201)

app.run(debug=True) ## -> colocando o serviço no ar