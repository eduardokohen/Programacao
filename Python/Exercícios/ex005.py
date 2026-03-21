#Faça um código que receba um número e mostre na tela seu sucessor e seu antecessor:

n=int(input('Digite um número: '))
a = n-1
s = n+1

print(f'O número escolhido foi {n}; \nSeu antecessor é {a}; \nSeu sucessor é {s}.')
print('O número escolhido foi {}; \nSeu antecessor é {}; \nSeu sucessor é {}.'.format(n, a, s))