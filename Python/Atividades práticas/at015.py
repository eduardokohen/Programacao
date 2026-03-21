from math import sqrt, floor

n = float(input('Digite um número: '))
m = sqrt (n)

print('A raiz quadrada de {} é {:.2f}'.format(n, m))
print('A raiz quadrada arredondada de {} é {}' .format(n, floor(m)))