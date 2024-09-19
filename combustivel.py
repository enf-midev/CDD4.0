combs = input("Gasolina ou Etanol ")
litros = float(input("Informe a quantidade: "))
G = 5.8
E = 4.9

if combs == "Gasolina":
    print(f"Combustivel utiizado: {combs}, quantidade abastecida: {litros} e valor pago: {litros*G:.2f}")