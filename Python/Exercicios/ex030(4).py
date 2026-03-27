magenta = '\033[1;35m'
verde = '\033[1;32m'
azul = '\033[1;34m'
vermelho = '\033[1;31m'
reset = '\033[m'

num = -1

while num != 0:
    num = int(input(f'{magenta}Digite um número ou 0 para sair: {reset}'))

    if num == 0:
        print(f'{verde}Você está saindo do jogo. Até logo!!!{reset}')

    elif num % 2 == 0:
        print(f'{azul}O número {num} é par.{reset}')

    else:
        print(f'{vermelho}O número {num} é ímpar.')