#Crie um programa que receba um número e diga se é par ou ímpar.

#Adicionando cores ao terminal:
magenta = '\033[1;35m'
verde = '\033[1;32m'
azul = '\033[1;34m'
reset = '\033[m'

num = int(input(f'{magenta}Digite um número: {reset}')) #Recebe um número do usuário

resultado = num % 2 #Calcula o resto da divisão por 2. 0 é par e 1 é ímpar

#Verifica se é par ou ímpar e imprime o resultado.
if resultado == 0:
    print(f'{azul}O número {num} é par.{reset}')
else:
    print(f'{verde}O número {num} é ímpar{reset}')