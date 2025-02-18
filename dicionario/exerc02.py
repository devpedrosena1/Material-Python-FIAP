def inverter_dicionario(dicionario):
    dicionario_invertido = {}
    for ingles, portugues in dicionario.items():
        dicionario_invertido[portugues] = ingles
    return dicionario_invertido

dicionario_original = {
    "apple" : "maçã",
    "dog" : "cachorro",
    "car" : "carro",
    "house" : "casa"
}

dicionario_invertido = inverter_dicionario(dicionario_original)
print(dicionario_invertido)