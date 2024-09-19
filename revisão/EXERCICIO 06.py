peso = float(input("Informe seu peso: "))
altura = float(input("Informe sua altura: "))
IMC = peso / (altura*altura)
if IMC <=18.5:
    print(f"Abaixo do peso")
elif IMC >= 18.6 and IMC < 25  :
    print(f"Peso Ideal! PARABÉNS")
elif IMC >=25.0 and IMC < 30 :
    print(f"Levemente acima do peso.")
elif IMC >=30.0 and IMC <35  :
    print(f"Obesidade grau I")
elif IMC >=35.0 and IMC<=40 :
    print(f"Obesidade grau II(severa)")
elif IMC >= 40:
    print(f"Obesidade grau III (mórbida) ")