#Desenvolva um programa que leia o peso e a altura de uma pessoa, calcule o IMC e mostre
#seu status de acordo com a tabela: abaixo de 18.5: abaixo do peso, entre 18.5 e 25: peso ideal,
#25 até 30: sobrepeso, 30 até 40: obesidade e acima de 40: obesidade mórbida.

from math import pow

altura = float(input('Informe a sua altura: '))
peso = float(input('Informe o seu peso: '))

imc = peso/pow(altura,2)

if imc < 18.5:
    condicao = 'abaixo do peso'
elif 18.5 <= imc < 25:
    condicao = 'com peso ideal'
elif 25 <= imc < 30:
    condicao = 'acima do peso'
elif 30 <= imc < 40:
    condicao = 'obeso'
else:
    condicao = 'obeso mórbido'

print('Você está {}.'.format(condicao))