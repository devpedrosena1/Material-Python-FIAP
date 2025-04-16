import requests
url = 'https://www.diretodostrens.com.br/api/status'
objeto = requests.get(url)

if objeto.status_code == 200:
    info = objeto.json()

    for linha in info:
        print(f"Número da linha: {linha['codigo']} -> {linha['situacao']}")

elif objeto.status_code == 400:
    print("Erro 400, verifique a linha informada")
else:
    print(objeto.status_code)