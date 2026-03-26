#Desenvolva um programa que leia o comprimento de três retas e diga ao usuário
#Se elas podem ou não formar um triângulo.

a = int(input('Informe a medida da primeira reta: '))
b = int(input('Informe a medida da segunda reta: '))
c = int(input('Informe a medida da terceira reta: '))

if (a + b > c and a + c > b and b + c > a):
    print(f'As retas {a}, {b} e {c} formam um triângulo!')

else:
    print(f'As retas {a}, {b} e {c} não formam um triângulo')