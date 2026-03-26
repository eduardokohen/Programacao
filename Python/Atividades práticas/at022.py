num = str(input('Digite um número com 6 dígitos: ')).strip()

lista = list(num)

lista[0], lista[1] = lista[1], lista[0]
lista[2], lista[3] = lista[3], lista[2]
lista[4], lista[5] = lista[5], lista[4]

novo_num = "".join(lista)

print('O novo número é: {}'.format(novo_num))