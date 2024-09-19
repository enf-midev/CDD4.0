opção = 1
while opção != 2 :
    n1 = int(input("Informe um número: "))
    if n1 % 2 == 0 and n1 < 0:
        print(f" O número é {n1} é PAR e NEGATIVO")
    elif n1 % 2 == 0 and n1 > 0:
        print(f" O número é  {n1} é PAR e POSITIVO")
    elif n1 % 2 != 0 and n1 > 0:
        print(f" O número é {n1} é IMPAR e POSITIVO")
    elif n1 % 2 != 0 and n1 < 0:
        print(f" O número é  {n1} é IMPAR e NEGATIVO")
    opção = int(input("Deseja repetir: DIGITE 1 para SIM e 2 para NÃO: "))