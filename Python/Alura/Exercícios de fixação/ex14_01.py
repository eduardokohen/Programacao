produtos = {
    "arroz": 25.90,
    "feijão": 8.50,
    "café": 18.00,
    "açúcar": 23.59
}

produto = str(input("Produto: ")).lower()

if produto in produtos:
    print(f"Preço: R$ {produtos[produto]:.2f}.")
else:
    print("Produto não cadastrado.")