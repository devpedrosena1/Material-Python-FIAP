def processaPartida(partida : str) -> str:
    partida = partida.replace("\n", "")
    campos = partida.split(" X ")

    time_a = campos[0].split(" ")
    time_b = campos[1].split(" ")

    resultado = []
    if len(time_a) == 2:
        resultado.append((time_a[0]))
        resultado.append(int(time_a[1]))
    else:
        resultado.append(f"{time_a[0]} {time_a[1]}")
        resultado.append(int(time_a[2]))
        
    if len(time_b) == 2:
        resultado.append((time_b[1]))
        resultado.append(int(time_b[0]))
    else:
        resultado.append(f"{time_b[1]} {time_b[2]}")
        resultado.append(int(time_b[0]))

    return resultado

def atualiza_tabela(time: str, pontos: int, tabela: dict) -> dict:
    if time in tabela:
        tabela[time] += pontos
    else:
        tabela[time] = pontos
    return tabela

if __name__ == "__main__":

    tabela = {}
    
    arq = open("arquivos/resultados.txt", mode="r", encoding="utf-8")
    dados = arq.readlines()
    for jogo in dados:
        result = processaPartida(jogo)

        mand = result[0]
        visit = result[2]

        if result[1] > result[3]:
            ## adiciona 3 pontos ao time vencedor
            atualiza_tabela(mand, 3, tabela)
            atualiza_tabela(visit, 0, tabela)

        elif result[3] > result[1]:
            ## adiciona 3 pontos ao time vencedor
            atualiza_tabela(visit, 3, tabela)
            atualiza_tabela(mand, 0, tabela)
        else:
            ## adiciona 1 ponto a cada time
            atualiza_tabela(mand, 1, tabela)
            atualiza_tabela(visit, 1, tabela)

    arq.close()
    for time in tabela:
        print(f"{time} -> {tabela[time]} pontos")
