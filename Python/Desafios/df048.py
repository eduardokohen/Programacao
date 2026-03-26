#Escreva um programa que pergunte o salário de um funcionário e calcule seu aumento.
#Se o salário é maior que 1250, aumente 10%. Se menor, aumente 15%.
#Os empregados que estão abaixo de 1250 não podem ganhar mais que os que estão acima.

sal = float(input('Informe qual é o salário: '))
corte = 1250
lim = 1437.5

if sal <= 1250:
    sal = sal * 1.15

elif 1250 < sal <= 1437.50:
    sal = 1437.5 * 1.1

else:
    sal = sal * 1.1

print('O salário reajustado é de {:.2f}'.format(sal))