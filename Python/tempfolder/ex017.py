#faça um programa que leia o cateto oposto, o cateto adjacente e calcule a hipotenusa.

from math import hypot
co = float(input('Informe a medida do cateto oposto: '))
ca = float(input('Informe a medida do cateto adjacente: '))
h = hypot(co,ca)

print('A medida da hipotenusa é {:.2f}'.format(h))