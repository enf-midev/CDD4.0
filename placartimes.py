time1 = input("escreva o primeiro time")
time2 = input("escreva o segundo time")
golst1 = int(input("escreva o número de gols do primeiro time"))
golst2 = int(input("escreva o número de gols do segundo time "))
if golst1 == golst2:
    print("EMPATE")
else:
    if golst1 > golst2:
        print(f"{time1} VENCEDOR . Placar {golst1}x{golst2}")
    else:
        print(f"{time2} VENCEDOR . Placar {golst2}x{golst1}")
