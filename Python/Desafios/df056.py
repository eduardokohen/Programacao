#Crie um código que peça ao usuário um número. Verifique se é ou não bissexto

from datetime import datetime

atual = datetime.now().year

ano = int(input('Informe um ano: '))

bissexto = (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0)

if bissexto:
    if (ano < atual):
        print(f'O ano de {ano} foi bissexto.')
    elif (ano == atual):
        print(f'O ano de {ano} é bissexto.')
    else:
        print(f'O ano de {ano} será bissexto.')   
else:
    if (ano < atual):
        print(f'O ano de {ano} não foi bissexto')
    elif (ano == atual):
        print(f'O ano de {ano} não é bissexto.')
    else:
        print(f'O ano de 1919{ano} não será bissexto')