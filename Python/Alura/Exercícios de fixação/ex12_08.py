meses = []

for i in range(12):
    mes = str(input(f"Informe o {i+1}º mês: ")).title()
    meses.append(mes)

meses = tuple(meses)

print()
print("Terceiro mês: ", meses[2])
print()

for mes in meses:
    print(mes)