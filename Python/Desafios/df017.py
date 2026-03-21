#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar
r = float(input('Digite o seu saldo em reais: '))
d = r/5.22

print('Com {:.2f} reais você pode comprar {:.2f} dólares' .format(r, d))