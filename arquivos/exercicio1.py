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

with open("arquivos/resultados.txt", mode="r") as arq:
    for i, item in enumerate(arq):
        times = item.split("X")

        if len(times) >= 2:
            print(times[0])
            print(times[1])
        else:
            print(f'Linha mal formatada: {item}')

        print(times)