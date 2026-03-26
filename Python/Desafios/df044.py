distancia = float(input('Informe a distância da viagem: '))

fixo = 200

if distancia <= fixo:
    preco = distancia * 0.5
    print(f'O valor da passagem é de R${preco:.2f}.')
else:
    preco = fixo*0.5 + ((distancia-fixo)*0.45)
    print(f'O valor da passagem é de R${preco:.2f}.')