#Faça um algoritmo que leia um valor em reais e diga quantos dólares é possível comprar com o valor digitado

r = float(input('Digite seu saldo em reais: '))

d = r/5.22
i = r*30.65

print('Com R$ {:.2f} é possível comprar US$ {:.2f} e JPY {:.2f}'.format(r, d, i))