valor_compra = float(input("Digite o valor da compra: "))

if valor_compra >= 200:
    desconto = valor_compra * 0.2
elif valor_compra >= 100:
    desconto = valor_compra * 0.1
elif valor_compra >= 50:
    desconto = valor_compra * 0.05
else:
    desconto = 0

valor_final = valor_compra - desconto

print("="*60)
print("Resumo da compra".center(60))
print("="*60)
print(f"""
Valor da compra: R$ {valor_compra:.2f}
Desconto: R$ {desconto:.2f}
Valor final: R$ {valor_final:.2f}""")
print("="*60)