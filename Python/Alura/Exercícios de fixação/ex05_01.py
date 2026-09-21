idade = int(input("Digite a idade: "))

if idade >= 18:
    print("Maior de idade.")
    if idade >= 60:
        print("Também está na faixa de 60 anos ou mais.")
else:
    print("Menor de idade.")