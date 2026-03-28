from datetime import datetime

while True:

    ano = int(input('Digite um ano (ou 0 para sair): '))

    if ano == 0:
        print('Encerrando...')
        break



    atual = datetime.now().year

    bissexto = (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0)

    def tempo_p (ano):
        if ano < atual:
            return "foi"
        elif ano == atual:
            return "é"
        else:
            return "será"
        
    tempo = tempo_p(ano)

    if bissexto:
        print(f'O ano {ano} {tempo} bissexto')
    else:
        print(f'O ano {ano} não {tempo} bissexto')