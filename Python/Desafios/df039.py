#Faça um programa que pense em um número secreto. O usuário deve tentar advinhar esse número
#Se acertar, parabenize. Se errar, diga que errou.

from random import randint

numero_secreto = randint(0,5)

palpite = int(input('Digite um número de 0 a 5: '))

if palpite == numero_secreto:
    print('Parabéns! Você acertou!')
else:
    print('Você errou!')