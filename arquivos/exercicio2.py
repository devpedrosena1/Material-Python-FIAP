if __name__ == "__main__":

    import random

    produtos = [
        "Celular", 
        "Smart TV", 
        "Notebook", 
        "Máquina de lavar"
    ]

    marcas = [
        ["Apple", "Samsumg"], ## celular
        ["LG", "Phillips"], # smart tv
        ["Asus", "Lenovo"], ## notebook
        ["Brastemp", "Eletrolux"] ## geladeira
    ]

    precos = [
        [2000, 7000], ## celular
        [3000, 8000], ## smarttv
        [1700, 2600], ## notebook
        [2000, 6000] ## geladeira
    ]

    lojas = ["Loja 1", "Loja 2", "Loja 3"] ## lojas

    faturamento_total = 0

    with open("arquivos/faturamento.txt", mode="w") as arq:
        for i in range(2000):
            i_produto = random.randint(0, len(produtos) -1)
            i_loja = random.randint(0, len(lojas) -1)
            i_marca = random.randint(0, 1)

            produto = produtos[i_produto]
            marca = marcas[i_produto][i_marca]
            loja = lojas[i_loja]

            # data
            dia = random.randint(1, 30)
            mes = random.randint(1, 12)
            ano = 2022
            data = f"{dia}/{mes}/{ano}"

            qtde_produtos = random.randint(1, 10)

            preco_unitario = random.randint(precos[i_produto][0], precos[i_produto][1])

            faturamento = qtde_produtos * preco_unitario
            faturamento_total = faturamento_total + faturamento

            linha_formatada = f"{produto};{marca};{loja};{data};{qtde_produtos};{preco_unitario}\n"


            arq.write(linha_formatada)

        arq.write("O faturamento foi de R${:,}\n".format(faturamento_total))

    print("Arquivo gerado com sucesso!")