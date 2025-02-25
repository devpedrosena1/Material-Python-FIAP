'''
criar um programa que mostre qual time teve mais pontos
e consequentemente o campeão. obs: podemos usar o metodo
.split() para separar a linha do arquivo em pedaços,
e assim percorrer cada linha e seus indices para comparar 
os resultados e consequentemente apontar o campeao.

regras: 

vitoria = 3pts
empate = 1pts
derrota = 0pts

'''

times = []
pontos = []

with open("arquivos/resultados.txt", mode="r") as arq:
    for item in arq:
        item = item.strip() ## remover espaços do inicio e do fim
        partes = item.split("X") ## dividir a string em dois

        ## viu se a divisão funcionou
        if len(partes) == 2:
            time1, time2 = partes

            placar = item.split("X")

            ## buscou a informação do placar ao respectivo
            ## time, dividindo com split tbm
            gols_time1 = int(placar[0].split()[1])
            gols_time2 = int(placar[1].split()[0])

            print(gols_time1, gols_time2)

            ## comparar o resultado do time 1 com o time 2
            # quem for maior vence, em caso de empate 1 pt para cada
            if gols_time1 > gols_time2:
                pontos[times.index(time1[0])] += 3
            elif gols_time2 > gols_time1:
                pontos[times.index(time2[1])] += 3
            else:
                pontos[times.index(time1)] += 1
                pontos[times.index(time2)] += 1

## determinando o time campeão
max_pontos = max(pontos) ## encontrando o maximo de pontos
indice_campeao = pontos.index(max_pontos)
campeao = times[indice_campeao]

print(f'O grande campeão foi: {campeao} com {max_pontos} pontos!')