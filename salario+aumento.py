nome = input("digite seu nome: ")
idade = int(input("digite sua idade: "))
salario = float(input("digite seu salário:"))
aumento = (salario *1.1)
meses = (idade *12)
print(f"Olá {nome}, você tem {idade} anos e {meses} meses. "
      f"\nSeu salário é: {aumento:,.2f}")