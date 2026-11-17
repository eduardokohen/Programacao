print('{:=^40}'.format('LOJAS KOHEN'))

preco = float(input("Preço das compras: R$ "))
print("""FORMAS DE PAGAMENTO: 

[1] À vista dinheiro/PIX
[2] À vista no cartão
[3] 2x no cartão
[4] 3x ou mais no cartão""")

opcao = int(input("\nQual é a opção: "))

if opcao == 1:
    total = preco * 0.9
elif opcao == 2:
    total = preco * 0.95
elif opcao == 3:
    total = preco
    parcela = total/2
    print(f"Sua compra será parcelada em 2x de R$ {parcela:.2f}.")
elif opcao == 4:
    total = preco * 1.2
    vezes = int(input("Digite a quantidade de parcelas: "))
    parcela = total/vezes
    print(f"Sua compra será parcelada em {vezes}x de R$ {parcela:.2f}.")
else:
    print("Opção inválida! Encerrando sessão...")
    exit()

print(f"Sua compra de R$ {preco:.2f} vai custar {total:.2f} no final.")