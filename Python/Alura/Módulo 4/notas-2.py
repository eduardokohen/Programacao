notas = []

for i in range(6):
    nota = float(input(f"Digite a {i+1}ª nota: "))
    notas.append(nota)

for nota in notas:

    if nota >= 9:
        print(f"{nota} - excelente.")
    elif nota >= 7:
        print(f"{nota} - bom.")
    elif nota >= 5:
        print(f"{nota} - regular.")
    else:
        print(f"{nota} - insuficiente")