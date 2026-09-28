numeros = []

for i in range(7):
    numero = int(input(f"Digite o {i+1}º número inteiro da lista: "))
    numeros.append(numero)

maior = max(numeros)
menor = min(numeros)
media = sum(numeros)/len(numeros)

texto = f"""
Lista completa dos numeros: {numeros}
Média dos números: {media:.2f}
Maior número da lista: {maior}
Índice do maior número da lista: {numeros.index(maior)}
Menor número da lista: {menor}
Índice do menor número da lista: {numeros.index(menor)}
"""

print(texto)