rep = 0
opcao = 1
while opcao !=2 and rep <= 3:
    neg=0
    for x in range (2):
        num = int(input("informe o número: "))
        if num < 0:
            neg = neg + 1
    print(f"quantidade de números negativos : {neg}")
    opcao = int(input("deseja repetir? 1 para SIM e 2 para NÃO: "))
    rep = rep + 1