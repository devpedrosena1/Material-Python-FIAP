if __name__ == "__main__":
    while True:
        try:
            nome = input('Informe o nome: ')
            dia_nasc = int(input('Dia do nascimento: '))

            print(f'{nome} nasceu no dia {dia_nasc}')
            break

            ## arq = open('excecoes/exemplo1.py', mode="r")
            ## print(arq)
            ## arq.close()
            ## tracebak.print_exc() -> informa o erro

        except Exception as e:
            print(f'Aconteceu um erro inesperado: {e}')

        ## podemos usar except ValueError, zeroDivisionError, KeyError, PermissionError
        ## fileNotFoundError, indexError

        ## uma boa pratica é tentar prever todos os erros possiveis com as estruturas 
        ## acima, mas é legal ter um except padrão caso não caia em nenhum erro que você
        ## "preveu"