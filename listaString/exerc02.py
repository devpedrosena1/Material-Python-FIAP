def colocar_espaco(palavra: str) -> str:
    resp = ''
    for letra in palavra:
        resp = resp + letra + ' '
    return resp

resposta = colocar_espaco(input('Digite a palavra: '))
print(resposta)

## git clone https://github.com/egondo/1tdsq.git