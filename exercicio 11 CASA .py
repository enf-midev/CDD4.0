litros = float(input("quatidade de litros: "))
tipo = input("Qual combustivel? ")
Gasolina = 5.8
Etanol = 4.9

if tipo == "g" or tipo == "G":
    print(f"Olá você abasteceu Gasolina, com {litros} e pagou {litros*Gasolina:.2f}")
elif tipo == "e" or tipo == "E":
    print(f"Olá você abasteceu Etanol, com {litros} e pagou {litros*Etanol:.2f}")
else:
    print("sentença incorreta")