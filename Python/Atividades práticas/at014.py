n1 = int(input('Um valor: '))
n2 = int(input('Outro valor: '))

s = n1+n2
m = n1*n2
d = n1/n2
di = n1//n2
p = n1**n2

print('A soma vale {};\nO produto vale {};\nA divisão vale {};\nA divisão inteira vale {}; ' .format(s, m, d, di,), end=' ')
print('E a potência vale {}.' .format(p))

#Com o "\n" se insere uma quebra de linha. Com o "end=''" se tira a quebra de linha de um print para outro.