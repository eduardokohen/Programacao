#Escreva um programa que leia a velocidade de um carro. 
#Se ele ultrapassar 80km/h mostre uma mensagem dizendo que ele foi multado.
#Informe o valor da multa, de R$7,00 por cada km acima do limite.

vel = float(input('Informe a velocidade aferida: '))
lim = 80
mul = 7*(vel-lim)

if vel > lim:
    print(f'Você ultrapassou o limite de {lim:.2f}km/h.')
    print(f'Você terá que pagar uma multa de R${mul:.2f}.')
else:
    print(f'Você está dentro do limite de velocidade. Parabéns!')