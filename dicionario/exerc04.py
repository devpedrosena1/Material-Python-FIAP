import os

'''
crie um dicionario onde a chave é o PIX da pessoa (cpnj/cpf, telefone, email)
e o valor é um outro dicionario que armazena os dados de uma conta (nome, banco,
numero da conta). Faça uma aplicação com duas opções no menu: Cadastrar chave pix 
e consultar chave pix. No cadastra devera ser informado a chave pix e as informações
do usuario. e na consulta o usuario aplica a chave pix e o sistema retorna as 
informações completas do usuario. obs: no cadastro, se a chave existir deve retornar
uma mensagem falando que a chave já está cadastrada, e na consulta, se a chave não
existir, devera ser relatado tambem o problema. 
'''

dic = {}

def limpar_tela():
    os.system('clear')

def cadastrar_chave_pix():
    try:
        print("=== Cadastrar chave PIX ===")
        chave = input("Digite a sua chave PIX: ")
        if chave in dic:
            print("Chave PIX já cadastrada!")
        else:
            nome = input("Informe o nome do usuário: ")
            banco = input("Informe o banco do usuário: ")
            num_conta = int(input("Informe o número da conta: "))

        ## armazena as informações no dicionario
        dic[chave] = {
            "nome" : nome,
            "banco" : banco,
            "num_conta" : num_conta
        }

        print("Cadastro de chave PIX realizado com sucesso!")

    except Exception as e:
        print(f"Ocorreu um erro durante o cadastro PIX: {e}")

    limpar_tela()

def consultar_chave():
    try: 
        print("=== Consultar chave PIX ===")
        chave = input("Digite a chave PIX para consulta: ")
        ## verifica se a chave existe 
        if chave not in dic:
            print("Chave PIX não encontrada!")
        else:
            ## exibir as informações cadastradas
            dados = dic[chave]
            print(f"Nome: {dados['nome']}")
            print(f"Banco: {dados['banco']}")
            print(f"Número da conta: {dados['num_conta']}")

    except Exception as e:
        print(f"Ocorreu um erro durante a consulta PIX: {e}")

    limpar_tela()

def menu():
    while True:
        try:
            print("=== Bem vindo ao sistema do banco! ===")
            print("1. Cadastrar chave PIX")
            print("2. Consultar chave PIX")
            print("3. Sair")

            opcao = input("Escolha uma opção: ")

            if opcao == '1':
                cadastrar_chave_pix()
            elif opcao == '2':
                consultar_chave()
            elif opcao == '3':
                print("Saindo...")
                break
            else:
                print("Ocorreu um erro no sistema...")

        except Exception as e:
            print(f"Ocorreu um erro inesperado no menu: {e}")

if __name__ == "__main__":
    menu()