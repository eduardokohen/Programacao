produtos = {
    "arroz": 25.90,
    "feijão": 8.90,
    "café": 18.59
}

produto = str(input("Produto: ")).lower()

if produto in produtos:
    print(f"Preço: R$ {produtos[produto]:.2f}.")
else:
    print(f"O produto {produto} não está cadastrado.")