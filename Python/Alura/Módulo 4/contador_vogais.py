palavra = str(input("Informe a palavra para contar as vogais: "))
vogais = "aeiouAEIOU"
contador_vogais = 0

for letra in palavra:
    if letra in vogais:
        contador_vogais += 1
        print(f"Esta é uma vogal: {letra}")

print(f"A palavra tem {contador_vogais} vogais.")