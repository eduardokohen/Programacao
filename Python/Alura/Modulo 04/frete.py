distancia = float(input("Digite a distância em quilômetros: "))
peso = float(input("Digite o peso em quilos: "))
vip = str(input("Você é cliente VIP? (s/n): ")).lower()

if distancia <= 50:
    frete_base = 10
    if peso >= 10:
        acrescimo = 5
    else:
        acrescimo = 0
elif distancia <= 200:
    frete_base = 20
    if peso >=10:
        acrescimo = 5
    else:
        acrescimo = 0
else:
    frete_base = 20
    if peso >= 10:
        acrescimo = 5
    else:
        acrescimo = 0

frete = frete_base + acrescimo

if vip == "s":
    desconto = frete * 0.1
    frete = frete - desconto
    eh_vip = "Sim"
else:
    desconto = 0
    frete = frete - desconto
    eh_vip = "Não"

print("="*60)
print("RESUMO DO FRETE".center(60))
print("="*60)
print(f"""
Distância: {distancia:.2f} km
Frete base: R$ {frete_base:.2f}
Peso: {peso:.2f} kg
Acréscimo de peso: R$ {acrescimo:.2f}
Cliente VIP: {eh_vip}
Desconto VIP: R$ {desconto:.2f}
------------------------------------------------------------
Valor final: R$ {frete:.2f}
""")
print("="*60)