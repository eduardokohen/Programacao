#Faça um código que calcule o preço de uma passagem. Para viagens de até 200km, R$0,50/km.
#Para viagens de mais de 200km, o preço do km é de R$0,45/km.

magenta = '\033[1;35m'
verde = '\033[1;32m'
azul = '\033[1;34m'
vermelho = '\033[1;31m'
ciano = '\033[1;36m'
reset = '\033[m'

ckm1 = 0.5
ckm2 = 0.45
corte = 200

while True:
    dist = float(input(f'{ciano}Informe a distância ou pressione 0 para sair: {reset}'))

    if dist == 0:
        print(f'{azul}Você está saindo do nosso aplicativo. Até breve!!!{reset}')
        break

    if dist < 0:
        print(f'{vermelho}Número inválido! Digite uma distância maior que 0!{reset}')
        continue

    if 0 < dist <= corte:
        valor = dist*ckm1
    else:
        valor = (corte*ckm1) + ((dist - corte)*ckm2)
    
    print(f'{magenta}Você está prestes a fazer uma viagem de {dist} km! Parabéns!{reset}')
    print(f'{verde}O valor da passagem é de R${valor:.2f}.')