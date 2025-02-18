## criando uma lista vazia para receber dados
produtos = []

## criando um loop para a navegação do usuario
while True:

    ## coletando as informações do produto
    codigo = int(input('Digite o código do produto: '))
    descricao = input('Dê uma descrição ao produto: ')
    quantidade = int(input('Digite a quantidade de produtos: '))
    valor = float(input('Digite o valor do produto: '))

    ## criando um dicionario pro produto
    produto = {
        "codigo" : codigo,
        "descricao" : descricao,
        "quantidade" : quantidade,
        "valor" : valor
    }

    ## armazenar esse dicionario dentro da lista produtos
    produtos.append(produto)

    ## vamos perguntar pro usuario se ele quer continuar acrescentando produtos na lista
    continuar = input('Deseja continuar? Se sim digite (S), se não, digite (N)').lower()
    if continuar == 'n':
        break

## exibir as informações coletadas
print('\nLista de produtos cadastrados: ')
for produto in produtos:
    print(f'Código: {produto['codigo']}, Descrição: {produto['descricao']}, Quantidade: {produto['quantidade']}, Preço: R$ {produto['valor']:.2f}')
