def substitui(frase: str, letras: str) -> str:
    resp = ''
    for c in frase:
        if c.lower() in letras.lower():
            resp += '*'
        else:
            resp += c
    return resp

frase_teste = 'I can only show you the door.\nYou’re the one that has to walk through it.'
letra_teste = 'aro'
resultado = substitui(frase_teste, letra_teste)
print(resultado)