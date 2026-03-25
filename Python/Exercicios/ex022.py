nome = str(input('Digite seu nome completo: ')).strip()
print('Analisando seu nome...')

separado = nome.split()

print(f'Seu nome em maiúsculas é {nome.upper()}')
print(f'Seu nome em minúsculas é {nome.lower()}')
print(f'Seu nome tem ao todo {len(nome.replace(" ", ""))} letras')
print(f'Seu primeiro nome é {separado[0]} e ele tem {len(separado[0].replace(" ", ""))} letras')