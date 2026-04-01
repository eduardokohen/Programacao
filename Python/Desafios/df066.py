import random

pc = random.randint(1,3)

if pc == 1:
    objeto = 'pedra'
elif pc == 2:
    objeto = 'papel'
else:
    objeto = 'tesoura'

print(objeto)

opcao = int(input('Faça sua jogada!\n1 - Pedra \n2 - Papel\n3 - Tesoura\n'))

if opcao == 1:
    jogador = 'pedra'
elif opcao ==2:
    jogador = 'papel'
elif opcao == 3:
    jogador = 'tesoura'

if ((jogador == 'pedra' and objeto == 'tesoura')or
    (jogador == 'tesoura' and objeto == 'papel')or
    (jogador == 'papel' and objeto == 'pedra')):
    print('Você venceu! Você escolheu {} e eu escolhi {}.'.format(jogador, objeto))

elif((jogador == 'tesoura' and objeto == 'pedra')or
     (jogador == 'papel' and objeto == 'tesoura')or
     jogador == 'pedra' and objeto == 'papel'):
    print('Você perdeu! Eu escolhi {} e você escolheu {}.'.format(objeto, jogador))

else:
    print('Empatamos! Você escolheu {} e eu escolhi {} também.'.format(jogador, objeto))