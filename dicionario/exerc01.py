texto = input('Digite uma palavra: ')
dic = {}

for letra in texto:
    if letra in dic:
        dic[letra] += 1
    else:
        dic[letra] = 1

for letra, quantidade in dic.items():
    print(f'A Letra {letra} aparece {quantidade} vezes.')

## hello world!!!
## espero que o commit vá