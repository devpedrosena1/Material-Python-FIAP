with open("arquivos/resultados.txt", mode="a") as arq:
    arq.write("Finalizando os resultados do campeonato")

    ## obs -> se não existir um arquivo chamado "resultados.txt"
    ## o metodo append CRIA um arquivo