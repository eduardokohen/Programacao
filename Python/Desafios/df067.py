import random

opcao = ['pedra', 'papel', 'tesoura']


while True:
    
    pc = random.choice(opcao)
    x = int(input('O que você escolhe? \n1 - Pedra? \n2 - Papel? \n3 - Tesoura?\n0 - Sair?\n'))
    
    if x == 0:
        break
    elif x == 1:
        eu = opcao[0]
    elif x == 2:
        eu = opcao[1]
    elif x ==3:
        eu = opcao[2]

    if ((eu == opcao[0] and pc == opcao[2])or
        (eu == opcao[1] and pc == opcao[0]) or
        (eu == opcao[2] and pc == opcao[1])):
        print('Você venceu! Você escolheu {} e eu escolhi {}.'.format(eu, pc))

    elif((eu == opcao[2] and pc == opcao[0])or
         (eu == opcao[0] and pc == opcao[1])or
        (eu == opcao[1] and pc == opcao[2])):
        print('Você perdeu! Você escolheu {} e eu escolhi {}.'.format(eu, pc))

    else:
        print('Empatamos! Você escolheu {} e eu escolhi {} também!'.format(eu, pc))