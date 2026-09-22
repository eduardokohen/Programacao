meses = []

for i in range(1,13,1):
    mes = input(f"Informe o {i}º mês: ").title()
    meses.append(mes)

meses = tuple(meses)

print()
print(f"Terceiro mês: {meses[2]}.")
print()

for mes in meses:
    print(mes)