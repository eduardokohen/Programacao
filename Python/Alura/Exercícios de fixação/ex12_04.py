meses = []

for i in range(12):
    mes = str(input(f"Informe o {i+1}º mês: "))
    meses.append(mes)

meses = tuple(meses)

print()
print(f"Terceiro mês: {meses[2]}.".title())
print()

for mes in meses:
    print(mes.title())
print()