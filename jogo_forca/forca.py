import palavras_forca 

def gera_segredo(word: str, chute: str) -> str:
    resp = ''
    for char in word:
        if char.lower() in chute:
            resp += char + " "
        else:
            resp += '_ '
    return resp


palavra = palavras_forca.get_country()
erros = 0
chutes = ' '
segredo = gera_segredo(palavra, chutes)


while (erros < 6 and '_' in segredo) :
    print(segredo)
    print(f'Erros: {erros}')

    letra = input('Letra: ')
    chutes += letra

    # verifica se a letra está na palava sorteada
    segredo = gera_segredo(palavra, chutes)

    if not letra in palavra.lower():
        erros += 1

if erros >= 6:
    print(f'Você foi enforcado! A palavra era: {palavra}')
else:
    print(f'Parabéns, você venceu!!!')

print(segredo)
print(f'Erros: {erros}')
letra = input('Letra: ')