import json

arquivo = open("arquivosJson/dados.txt", mode="r", encoding="utf-8")

dado = json.load(arquivo)
print(dado)