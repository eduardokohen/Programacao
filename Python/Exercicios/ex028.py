from random import randint

num = randint(0,100)

print('*** Bem vindo ao jogo do número secreto! ***')
tentativa = int(input('Faça sua tentativa. Digite um número aleatório e 0 a 100: '))

if (tentativa < num):
    print('Ih, você chutou muito baixo! Tente novamente.')

elif (tentativa > num):
    print('Ih, você chutou muito alto. Tente novamente!')

else:
    print('Parabéns! Você acertou!')