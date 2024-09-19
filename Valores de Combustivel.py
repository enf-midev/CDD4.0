combs = input("Digite G para Gasolina e E para Etanol:")
litros = float(input("Informe a quantidade do combustivel:"))
gasolina = 5.8
etanol = 4.9
if combs == "G" or combs == "g":
    print(f"Combustivel selecionado: Gasolina, abastecido:{litros}L \n e "
          f"pago: {gasolina * litros:.2f}")
elif combs == "E" or combs == "e":
    print(f"Combustivel selecionado: Etanol, abastecido: {litros} \n e"
              f"pago: {etanol * litros:.2f}")
else:
    print("opção invalida")


