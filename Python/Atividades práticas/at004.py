#Usando o .format
n1=int(input('Digite um valor: '))
n2=int(input('Digite outro: '))
s = n1 + n2
print('A soma entre {} e {} vale {}.'.format(n1,n2,s))
#Usando o fstring
print(f'A soma entre {n1} e {n2} vale {s}')
#usando concatenação
print('A soma entre ' + str(n1) + ' e ' + str(n2) + ' vale ' + str(s) + '.')