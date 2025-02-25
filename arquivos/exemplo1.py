with open("arquivos/dados.txt", "r") as arq:
    dados = arq.read()

print(dados)

## arq open(dados.txt, "r")
## dados = arq.read()
## arq.close()
## print(dados) -> ambos os códigos são equivalentes
##                 mudando apenas que, com o 'with'
##                 não precisamos fechar o arquivo.

