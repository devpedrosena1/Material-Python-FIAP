def frase_letra(frase: str, letra: str) -> str:
    resultado = ''
    for char in frase:
        if char.lower() == letra.lower():
            resultado += '*'
        else:
            resultado += char
    return resultado

frase_teste = 'Jabuticaba'
letra_teste = 'a'
resultado = frase_letra(frase_teste, letra_teste)
print(resultado)