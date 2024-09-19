opcao = 1
while opcao !=2:
    nota1 = float(input("Receba a 1ª nota: "))
    while nota1 < 0 or nota1 > 10:
        nota1 = float(input("Valor incorreto. Informe a nota novamente. 1ª nota: "))
    nota2 = float(input("Receba a 2ª nota: "))
    while nota2 < 0 or nota2 > 10:
        nota2 = float(input("Valor incorreto. Informe as notas novamente. 2ª nota: "))
    media = (nota1 + nota2) / 2
    print(f"A média do aluno foi:{media}")
    opcao = int(input("deseja repetir? 1 para SIM e 2 para NÃO: "))
