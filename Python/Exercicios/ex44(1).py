print("="*30)
print("LOJAS KOHEN".center(30, '='))
print("="*30)

valor = float(input("Digite o valor da compra: "))

texto = f"""Qual será a forma de pagamento? 
1) À vista em dinheiro ou cheque 
2) À vista no cartão
3) Em até 2x no cartão
4) Em 3x ou mais no cartão
"""

print(texto)

opcao = int(input("Digite sua opção: "))

if opcao == 1:
    valor_final = valor - (valor*0.1)
elif opcao == 2:
    valor_final = valor - (valor*0.05)
elif opcao == 3:
    valor_final = valor
elif opcao == 4:
    valor_final = valor * 1.2
else:
    print("Opção inválida! Encerrando sessão.")

print(f"O valor da compra é de R$ {valor:.2f}. O valor final é de {valor_final:.2f}.")