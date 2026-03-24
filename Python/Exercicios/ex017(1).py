co = float(input('Informe a medida do cateto oposto: '))
ca = float(input('Informe a medida do cateto adjacente: '))
h = (co**2 + ca**2)**(1/2)

print('A medida da hipotenusa é {:.2f}'.format(h))