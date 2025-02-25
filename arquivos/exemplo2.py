import random

times = ["Palmeiras", "Botafogo", "Flamengo", "Corinthians", "São Paulo", "Santos"]

with open("arquivos/resultados.txt", mode="w") as arq:
    for i in range(len(times)):
        for j in range(i+1, len(times)):
            gc = random.randint(0, 5)
            gv = random.randint(0, 5)
            arq.write(f"{times[i]} {gc} X {gv} {times[j]}\n")

    for i in range(len(times)):
        for j in range(i+1, len(times)):
            gc = random.randint(0, 5)
            gv = random.randint(0, 5)
            arq.write(f"{times[j]} {gc} X {gv} {times[i]}\n")