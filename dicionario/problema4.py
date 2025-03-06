import json

def menu():
    print("1. Cadastra")
    print("2. Consulta")
    print("3. Sair")
    opcao = int(input("Escolha uma opção: "))
    return opcao

def leitura_arquivo() -> dict:
    try:
        ##print("Lendo arquivo...")
        with open("dicionario/pix.json", "r", encoding="utf-8") as arq:
            retorno = json.load(arq)
            return retorno
    except FileNotFoundError:
        return {} ## se o arquivo não existir, retorna um dicionário vazio
    except Exception as e:
        print(f"Ocorreu um erro na leitura do arquivo: {e}")
        return {}
        

def cadastro(info: dict):
    ##print("Cadastrando...")
    chave = input("Informe a chave PIX: ")
    if chave in info:
        print("Essa chave PIX já existe!")
    else:
        nome = input("Informe o nome do usuário: ")
        doc = input("Informe o documento do usuário: ")
        banco = input("Informe o banco do usuário: ")
        conta = input("Informe o número da conta: ")

        valor = {"nome": nome, 
                 "doc": doc, 
                 "banco": banco, 
                 "conta": conta
                }
        info[chave] = valor

def consulta(info: dict) -> object:
    ##print("Consultando...")
    chave = input("Informe a chave PIX: ")
    if chave in info:
        return info[chave]
    else:
        return "Chave PIX não encontrada!"

def gravacao_arquivo(info: dict):
    ##print("Gravando arquivo...")
    with open("dicionario/pix.json", "w", encoding="utf-8") as arq:
        json.dump(info, arq, indent=2)

if __name__ == "__main__":
    print("Sistema Chave PIX")
    escolha = menu()

    dados = leitura_arquivo()

    while escolha != 3:
        if escolha == 1:
            cadastro(dados)
        elif escolha == 2:
            resultados = consulta(dados)
            print(resultados)
        elif escolha != 3:
            print("Opção inválida!")
        
        escolha = menu()

    gravacao_arquivo(dados)