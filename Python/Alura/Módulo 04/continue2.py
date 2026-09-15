numeros = []

for i in range(6):
    num = int(input(f"Digite o {i+1}º número: "))
    numeros.append(num)

for num in numeros:
    if num <= 0:
        continue
    print(num)