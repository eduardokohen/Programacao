#Faça um programa que leia os catetos oposto e adjacente e calcule a hipotenusa

import math

CO = float(input('Insira o valor do cateto oposto: '))
CA = float(input('Insira o valor do cateto adjacente: '))

H = math.sqrt(pow(CO, 2) + pow(CA, 2))

print('A hipotenusa é {:.2f}'.format(H))