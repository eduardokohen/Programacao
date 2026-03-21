#Faça um programa que lê um número inteiro e mostre na tela o seu sucessor e seu antecessor

n1 = int(input('Digite um número: '))
a = n1 - 1
s = n1 + 1

print('O número fornecido é {}, seu antecessor é {} e seu sucessor é {}'.format(n1, a, s))