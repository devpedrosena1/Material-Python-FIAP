import json

livro = {
    "Titulo" : "Harry Potter e a Pedra Filosofal",
    "Autor" : "J. K. Rowlling",
    "Ano" : 1997,
    "Original" : "Harry Potter and Phillosopher's Stone",
    "Generos" : ["Ficcao", "Infantil", "Drama"]
}

arquivo = open("arquivosJson/dados.txt", mode="w", encoding="utf-8")
json.dump(livro, arquivo, indent=4)
arquivo.close()

print("Programa finalizado!")