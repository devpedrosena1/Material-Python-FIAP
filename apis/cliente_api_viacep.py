import requests

cep = '04701-000'
url = f'https://viacep.com.br/ws/{cep}/json'

objeto = requests.get(url) # retirna um objeto, e não o json ainda
# print(type(objeto))

if objeto.status_code == 200:
    info = objeto.json()
    print(info)
elif objeto.status_code == 400:
    print("Erro 404.")
else:
    print(objeto.status_code)