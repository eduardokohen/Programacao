#Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário com 15% de aumento

s = float(input("Informe o salário: "))
a = s * 1.15

print('O salário é: {:.2f}. Com o aumento, vai para: {}'.format(s,a))