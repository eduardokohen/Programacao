produtos = []
precos = []
quantidades = []
totais = []

while True:
    produto = input("Digite o produto ou 'fim' para encerrar: ").title()

    if produto == "Fim":
        break

    preco = float(input(f"Digite o preço de {produto}: R$ "))
    quantidade = int(input(f"Digite a quantidade de {produto}: "))

    preco_bruto = preco * quantidade

    if quantidade > 3:
        desconto = preco_bruto * 0.05
    else:
        desconto = 0

    total_com_desconto = preco_bruto - desconto

    produtos.append(produto)
    precos.append(preco)
    quantidades.append(quantidade)
    totais.append(total_com_desconto)

print("\n========== RECIBO ==========")

valor_total = 0

for i in range(len(produtos)):
    preco_bruto = precos[i] * quantidades[i]

    print(f"\nProduto: {produtos[i]}")
    print(f"Quantidade: {quantidades[i]}")
    print(f"Preço unitário: R$ {precos[i]:.2f}")
    print(f"Preço bruto: R$ {preco_bruto:.2f}")
    print(f"Preço com desconto: R$ {totais[i]:.2f}")

    valor_total += totais[i]

print("\n-----------------------------")
print(f"TOTAL DA COMPRA: R$ {valor_total:.2f}")
print("=============================")