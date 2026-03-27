from random import randint
from time import sleep

print('*** Bem vindo ao jogo do número secreto! ***')
num = randint(1, 100)
tentativa = -1
contador = 0

while (tentativa != num):
    tentativa = int(input('Digite um número entre 1 e 100, ou digite 0 para sair: '))

    if (tentativa == 0):
        print('Desistiu? Volte novamente!')
        break
    
    contador += 1

    print('*** PROCESSANDO ***')
    sleep(3)

    if (100 >= tentativa > num):
        print('Você chutou muito alto! Tente novamente!')
    elif(tentativa < num):
        print('Você chutou muito baixo! Tente novamente!')
    elif(tentativa > 100):
        print('Número inválido! Digite um número entre 1 e 100!')
    else:
        print('Parabéns! Você acertou em {} tentativas!'.format(contador))