numeros = (18, 7, 25, 3, 42, 11, 9)

maior = max(numeros)
menor = min(numeros)
media = sum(numeros)/len(numeros)

texto = f"""
Lista de todos os números: {numeros}
Média de todos os números: {media:.2f}
Maior número da lista: {maior}
Posição do maior número da lista: {numeros.index(maior)}
Menor número da lista: {menor}
Posição do menor número da lista: {numeros.index(menor)}
"""

print(texto)