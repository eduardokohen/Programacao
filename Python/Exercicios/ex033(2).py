a = int(input('Primeiro valor: '))
b = int(input('Segundo valor: '))
c = int(input('Terceiro valor: '))

menor = a
maior = a

if b < a and b < c:
    menor = b
elif c < a and c < b:
    menor = c

if b > a and b > c:
    maior = b
elif c > a and c > b:
    maior = c

print(f'O maior valor é {maior}.')
print(f'O menor valor é {menor}.')