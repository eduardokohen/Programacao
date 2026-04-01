#Faça um código que calcule o valor a ser pago por um produto considerando seu preço normal
#e a condição de pagamento. À vista: 10%. À vista no cartão: 5%. Em até 2x no cartão: preço normal
#3 vezes ou mais no cartão: 20% de juros.

valor = float(input('Informe o preço do produto: '))
opcao = int(input("""Escolha uma opção de pagamento: 
                  1 - À vista:
                  2 - À vista no cartão:
                  3 - 2 vezes no cartão:
                  4 - 3 vezes ou mais no cartão: \n"""))

if opcao == 1:
    valor = valor*0.9
    tipo = 'à vista'
elif opcao == 2:
    valor = valor*0.95
    tipo = 'em uma vez no cartão'
elif opcao == 3:
    tipo = 'em duas vezes no cartão'
    valor = valor
elif opcao == 4:
    valor = valor*1.2
    tipo = 'em 3 vezes no cartão'
else:
    exit()

print('Você pagará {} pelo produto {}.'.format(valor, tipo))