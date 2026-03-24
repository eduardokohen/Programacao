#Crie um programa que leia os catetos oposto e adjacente e calcule a hipotenusa

import math

CO = float(input('Digite o valor do cateto oposto: '))
CA = float(input('Digite o valor do cateto adjacente: '))

print('O valor da hipotenusa é {:.2f}'.format(math.hypot(CO, CA)))