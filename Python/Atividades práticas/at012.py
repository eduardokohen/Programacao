n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
a = n1 + n2
s = n1 - n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
p = n1 ** n2
r = n1 % n2

print('A soma entre {} e {} é {}' .format(n1, n2, a))
print('A subtração entre {} e {} é {}' .format(n1, n2, s))
print('A multiplicação entre {} e {} é {}' .format(n1, n2, m))
print('A divisão entre {} e {} é {}' .format(n1, n2, d))
print('{} elevado a {} é {}' .format(n1, n2, p))
print('A divisão inteira entre {} e {} é {}' .format(n1, n2, di))
print('O resto da divisão entre {} e {} é {}' .format(n1, n2, r))