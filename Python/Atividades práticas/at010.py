#Fazendo várias operações aritméticas com dados do usuário
n1 = int(input('Digite um número: '))
n2 = int (input('Digite outro número: '))
s = n1+n2
m = n1*n2
d = n1/n2
di = n1//n2
e = n1**n2
print('A soma entre {} e {} vale {}'.format(n1, n2, s))
print('A multiplicação entre {} e {} vale {}'.format(n1, n2, m))
print('A divisão entre {} e {} vale {:.3f}'.format(n1, n2, d)) #:.3f - limita em 3 casas decimais
print('A divisão inteira entre {} e {} vale {}'.format(n1, n2,di))
print('{} elevado a {} é {}'.format(n1, n2, e), end=' ')#end='': determina que não haja quebra de linha 
print('FIM!')
