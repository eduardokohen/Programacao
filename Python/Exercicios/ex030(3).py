#Crie um programa que receba um número e diga se é par ou ímpar.

#Adicionando cores ao terminal:
magenta = '\033[1;35m'
verde = '\033[1;32m'
azul = '\033[1;34m'
vermelho = '\033[1;31m'
reset = '\033[m'

while True:
    num = int(input(f'{magenta}Digite um número ou 0 para sair: {reset}'))
    resultado = num % 2

    if num == 0:
        print(f'{vermelho}Você está saindo do jogo. Obrigado!{reset}')
        break

    if resultado == 0:
        print(f'{verde}O número {num} é par.{reset}')
    else:
        print(f'{azul}O número {num} é ímpar.{reset}')