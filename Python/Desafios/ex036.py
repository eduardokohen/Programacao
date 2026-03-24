#Faça um programa que leia o nome completo de uma pessoa mostrando em seguida o primeiro e o último nome

nome = input('Digite o nome completo: ')

novo_nome = nome.split()

print('O primeiro nome é {}' .format(novo_nome[0]))
print('O último nome é {}'.format(novo_nome[-1]))