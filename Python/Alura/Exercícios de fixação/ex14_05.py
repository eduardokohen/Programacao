produtos = {
    "Arroz": 25.90,
    "Feijão": 8.49,
    "Café": 18.90
}

produto = str(input("Produto: ")).title()

if produto in produtos:
    print(f"Preço: R$ {produtos[produto]:.2f}.")
else:
    print(f"O produto {produto} não está cadastrado.")