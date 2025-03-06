import json

arquivo = open("arquivosJson/dados_exercicio.txt", mode="r", encoding="utf-8")
dado = json.load(arquivo)

print("Dados gerados com sucesso!")
print(dado)