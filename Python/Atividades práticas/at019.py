frase = "Curso em Vídeo Python"

print(frase[9:21]) #Imprime as letras entre as posições 9 e 21 da string.
print(frase[9:21:2]) #Imprime as letras entre as posições 9 e 21 pulando de 2 em 2.
print(frase[:5]) #Começa no início e vai até a posição 5
print(frase[15:]) #Começa na posição 15 e vai até o final
print(frase[9::3]) #Começa no 9 e vai até o final, pulando de 3 em 3
print(len(frase)) #Mostra quantos caracteres há na string frase
print(frase.count("o")) #Conta quantas letras o existem na string
print(frase.count("o", 0, 13)) #Conta quantas letras o existem entre as posições 0 e 13
print(frase.find("deo")) #Mostra em que posição começou o fragmento deo
print(frase.find('Android')) #Retorna o valor -1 que significa que não existe Android dentro da string
print('Curso' in frase) #Retorna true porque há Curso na string
print(frase.replace('Python', 'Android')) #Substitui Python por Android
print(frase.upper()) #Converte tudo em caixa alta
print(frase.lower()) #Converte tudo em minúscula
print(frase.capitalize()) #Coloca só a primeira letra em maíscula
print(frase.title()) #Coloca maiúscula inicial em todas as palavras