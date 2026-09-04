idade = int(input("Digite a sua idade: "))
if idade < 16:
    voto = "não pode votar."
elif (idade >= 16 and idade < 18) or idade >= 70:
    voto = "pode votar, mas não é obrigado."
elif idade >= 18 and idade < 70:
    voto = "é obrigado a votar."

print(f"Você {voto}")