#Crie um programa que leia o nome completo de uma pessoa e mostre:
#O nome com todas as letras maísculas;
#O nome com todas as letras minúsculas;
#Quantas letras ao todo (sem considerar espaços)
#quantas letras tem o primeiro nome

nome = input('Digite seu nome completo: ')

print (nome.upper())
print (nome.lower())
print (len(nome.replace(" ", "")))
pnome = nome.split()
print (len(pnome[0]))