#Faça um programa que leia os catetos oposto e adjacente e calcule a hipotenusa

import math

CO = float(input('Insira o valor do cateto oposto: '))
CA = float(input('Insira o valor do cateto adjacente: '))

H = math.hypot(CO,CA)

print ('A hipotenusa é {:.2f}'.format(H))