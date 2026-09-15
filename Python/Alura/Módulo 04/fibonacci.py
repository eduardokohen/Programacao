limite_termos = int(input("Qual número você gostaria de ver a sequência de Fibonacci? "))
limite_valor = 100

texto = f"""
{"==="*10}
{"FIBONACCI".center(30)}
{"==="*10}
"""
print(texto)

fibonacci = [0,1]

for valor in range(2,limite_termos):
    proximo = fibonacci[valor-1] + fibonacci[valor-2]
    fibonacci.append(proximo)

print(fibonacci)