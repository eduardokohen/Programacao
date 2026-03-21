#Faça um programa que receba o valor do salário e mostre na tela esse valor corrigido em 15%

sal = float(input('Informe o salário: R$ '))
rea = 0.15*sal
n_sal = sal + rea

print('O novo salário é de R$ {}.'.format(n_sal))