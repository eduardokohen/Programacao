#Faça um programa que leia o preço de um produto e mostre seu novo preço com desconto de 5%

produto = input('Qual é o produto? ')
preco = float(input('Qual é o preço do {} '.format(produto)))

desconto = preco * 0.95

print('O preço do {} com desconto é de {:.2f}'.format(produto, desconto))