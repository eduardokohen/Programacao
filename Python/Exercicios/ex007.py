#Escreva um código que leia duas notas e tire sua média aritmética

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))

m = (n1+n2)/2

print('A primeira nota é {}; \nA segunda nota é {}; \nA média das notas é {:.2f}'.format(n1, n2, m))
print(f'A primeira nota é {n1}; \nA segunda nota é {n2}; \nA média das notas é {m:.2f}')