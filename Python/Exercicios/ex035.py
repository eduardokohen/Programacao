#Faça um programa que leia uma frase e mostre:
#Quantas vezes tem a letra a;
#Em que posição ela aparece pela primeira vez;
#Em que posição ela aparece a última vez;

frase = input('Digite uma frase: ')

print('A letra a aparece {} vezes na frase'.format(frase.count('a')))
print('A primeira vez que aparece é na posição {}'.format(frase.find('a')))
print('A última vez que aparece é na posição {}'.format(frase.rfind('a')))