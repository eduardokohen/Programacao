#Faça um programa que leia um ângulo qualquer e mostre os seus valores de seno, cosseno e tangente

import math

ang = float(input('Digite a medida do ângulo: '))
rad = math.radians(ang)

s = math.sin(rad)
c = math.cos(rad)
t = math.tan(rad)

print('O ângulo mede {}. \nO valor do seno é {:.2f}. \nO valor do cosseno é {:.2f}. \nO valor da tangente é {:.2f}'.format(ang, s, c, t))