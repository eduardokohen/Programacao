nome = input('Digite o nome completo: ').strip()

partes = nome.split()

primeiro = partes[0]
ultimo = partes[-1]

print(f'O primeiro nome é {primeiro}')
print(f'O último nome é {ultimo}')