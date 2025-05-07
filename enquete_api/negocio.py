import banco
import traceback

def recupera_perguntas(enquete: int) -> list:
    try:
        perguntas = banco.recupera_perguntas(enquete)

        # como os dados devem ser arrumados para facilitar a aplicação da enquete?
        # lista = [
        #     {"id": 1, "numero": 1, "questao": "qual o time que você torce?",
        #     "tipo": "aberta", "itens": []},

        #     {"id": 2, "numero": 2, "questao": "quem vai ganhar?",
        #     "tipo": "unica", "itens": ["Barcelona", "Inter"]},

        #     {"id": 3, "numero": 3, "questao": "Quais são os melhores jogadores da Champions?",
        #     "tipo": "multipla", "itens": ["Lautaro", "Lamine Yamal", 'Raphinha']}
        # ]

        # perguntas = []

        # for item in lista:
        #     id = item['id']
        #     numero = item['numero']
        #     questao = item['questao']
        #     tipo = item['tipo']
        #     itens = item['itens']
    
        #     dic = {'id': id, 'numero': numero, 'questao': questao, 'tipo': tipo, 'itens': itens}
        #     perguntas.append(dic)

        # print(perguntas)

        colecao = []
        aux_id = -1
        registro = None
        
        for dado in perguntas:
            if aux_id != dado[0]:
                aux_id = dado[0]
                if registro != None:
                    colecao.append(registro)
                registro = {
                    "id": dado[0],
                    "numero": dado[1],
                    "questao": dado[2],
                    "tipo": dado[3],
                    "itens": []
                }
            registro['itens'].append(dado[4])
        colecao.append(registro)
        return colecao

    except Exception as erro:
        traceback.print_exc()
        raise erro
    
if __name__ == "__main__":
    dados = recupera_perguntas(1)
    for reg in dados:
        print(reg)
