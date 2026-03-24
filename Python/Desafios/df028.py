#Um professor quer sortear a ordem de apresentação dos trabalhos de seus alunos. 
#Faça um programa que leia 4 nomes dos alunos e mostre a ordem sorteada.

import random

n1 = input('Digite o nome do primeiro aluno: ')
n2 = input('Digite o nome do segundo aluno: ')
n3 = input('Digite o nome do terceiro aluno: ')
n4 = input('Digite o nome do quarto aluno: ')

lista = [n1, n2, n3, n4]

random.shuffle(lista)

print ('A ordem de apresentação será: ', lista)