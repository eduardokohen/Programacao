from datetime import datetime

ano = datetime.now().year

while True:

    niver = int(input('Informe o ano do seu nascimento ou 0 para sair: '))
    tipo = ano - niver

    if niver > ano:
        print('Ano inválido! Digite um ano até {}!'.format(ano))
        continue
    elif niver == 0:
        print('Você está saindo do programa. Até logo!!!')
        break
    else:

        if tipo < 18:
            print('Ainda faltam {} anos para o seu alistamento'.format(18 - tipo))
        elif tipo == 18:
            print('Está na hora do seu alistamento militar! Aliste-se já!')
        else:
            print('Você devia ter se alistado há {} anos atrás.'.format(tipo - 18))