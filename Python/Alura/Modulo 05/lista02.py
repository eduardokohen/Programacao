#Criando a lista:
numeros = []

for i in range(5):
    num = int(input(f"Digite o {i+1}º número da lista: "))
    numeros.append(num)

#Tamanho da lista:
print(f"O tamanho da lista é: {len(numeros)}.")

#Somando todos os termos: 
print(f"A soma de todos os valores da lista é: {sum(numeros)}.")

#Ordenando os termos:
print(f"A lista ordenada é: {sorted(numeros)}.")
print(numeros)

#Contando ocorrências:

print(f"A lista possui {numeros.count(1)} vezes o número 1.")

#Ordenando com o sort:
numeros.sort()
print(numeros)