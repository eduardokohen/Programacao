produtos = {
    "arroz": 25.90,
    "feijão": 8.90,
    "café": 17.80
}

produto = input("Produto: ").lower()

if produto in produtos:
    print(f"Preço: R$ {produtos[produto]:.2f}.")
else:
    print(f"O produto {produto} não está cadastrado.")