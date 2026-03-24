import math

co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
h = math.hypot(co,ca)

print('O comprimento da hipotenusa é {:.2f}'.format(h))