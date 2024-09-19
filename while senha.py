senha = 0000
num = int(input("Informe sua senha: "))
tent = 1
while num != senha and tent<3:
    num = int(input(f"Senha Incorreta.\n Você tem {3-tent} chances.\n Informe sua senha: "))
    tent+=1
if tent == 3 and num != senha:
    print(f"Senha Bloqueada")
else:
    print(f"Login efetuado com sucesso.")


