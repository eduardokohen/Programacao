print("="*60)
print("FIBONACCI")
print("="*60)

a = 0 
b = 1

n = int(input("Informe a quantidade de termos: "))

for i in range(n):
    print(a, end = " ")

    novo_a = b
    novo_b = a + b

    a = novo_a
    b = novo_b

print()