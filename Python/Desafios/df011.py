#tabuada automatizada
n = int(input('Digite o número que você quer saber a tabuada: '))

for i in range(1,11):
    print('{} x {} = {}'.format(n, i, n*i))