from datetime import datetime #importa o módulo datetime para atualizar o ano automaticamente

ano_atual = datetime.now().year #Atualiza o ano do programa automaticamente

ano = int(input('Informe o ano: ')) #recebe o ano do usuário

bissexto = (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0) #verifica se o ano é bissexto

if ano < ano_atual: #Passado
    if bissexto:
        print(f'O ano {ano} foi bissexto.')
    else:
        print(f'O ano {ano} não foi bissexto.')

elif ano == ano_atual: #Presente
    if bissexto:
        print(f'O ano {ano} é bissexto.')
    else:
        print(f'O ano {ano} não é bissexto')

else: #Futuro
    if bissexto:
        print(f'O ano {ano} será bissexto')
    else:
        print(f'O ano não será bissexto.')