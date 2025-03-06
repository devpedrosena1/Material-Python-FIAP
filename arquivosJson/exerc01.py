import json

lista = []

time = {
    "Nome" : "Sao Paulo",
    "divisao" : "Serie A",
    "Estadio" : "Morumbi",
    "Fundacao" : 1930
}

time2 = {
    "Nome" : "Corinthians",
    "divisao" : "Serie A",
"Estadio" : "Neo Quimica Arena",
    "Fundacao" : 1910
}

lista.append(time)
lista.append(time2)

arquivo = open("arquivosJson/dados_exercicio.txt", mode="w", encoding="utf-8")
json.dump(lista, arquivo, indent=4)
arquivo.close()

print("Programa finalizado!")