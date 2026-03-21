#Faça um programa que leia um valor de um produto e mostre um novo valor com 5% de desconto

v = float(input('Qual é o valor do produto? R$ '))
d = 0.05*v
nv = v - d

print('O valor original do produto é R$ {:.2f}. Com o desconto de 5% da promoção o valor é {:.2f}'.format(v, nv))