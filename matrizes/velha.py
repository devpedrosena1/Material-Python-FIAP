## função para criar o tabuleiro
def criaTabuleiro():
    matriz = []
    i = 0

    while i < 3:
        matriz.append([' '] * 3)
        i+=1

    for linha in matriz:
        print(linha)

    return matriz

## função para verificar se há espaços vazios
def temEspaco(matriz):
    for linha in matriz:
        if ' ' in linha:
            return True
    return False

## função para verificar se houve um ganhador
def haGanhador(matriz):
    ## verificando linhas
    for linha in matriz:
        if linha[0] and linha[1] and linha[2] and linha[0] != ' ':
            return True
        
    ## verificando colunas
    for col in range(3):
        if matriz[0][col] == matriz[1][col] == matriz[2][col] and matriz[0][col] != ' ':
            return True
        
    ## verificando diagonais
    if matriz[0][0] == matriz[1][1] == matriz[2][2] and matriz[0][0] != ' ':
        return True
    if matriz[0][2] == matriz[1][1] == matriz[2][0] and matriz[0][2] != ' ':
        return True
        
## função para efetuar a jogada
def joga(matriz, lin, col, jogador):
    lin = int(input('Informe a linha que quer jogar.'))
    col = int(input('Informe a coluna que quer jogar.'))


if __name__ == "__main__":
    tabuleiro = criaTabuleiro()

    if temEspaco(tabuleiro):
        print('Ainda tem espaços vazios!')
    else:
        print('Não há mais espaços vazios!')

    if haGanhador(tabuleiro):
        print('Parabéns, você ganhou!')
    else:
        print('Poxa, você perdeu!')
