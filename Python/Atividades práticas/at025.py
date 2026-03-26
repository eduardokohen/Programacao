from datetime import datetime

anof = int(input('Qual é o ano de fabricação do seu carro: '))

anoa = datetime.now().year
tempo = anoa - anof

if tempo <= 3:
    print('Seu carro está novinho!')
elif 3 <= tempo <= 5:
    print('Seu carro está seminovo!')
else:
    print('Seu carro já está velho!')