n = 1
soma = 0
num = int(input("INFORME A QUANTIDADE DE ALUNOS: "))
while n < num + 1 :
    nota = float(input("INFORME AS NOTAS: "))
    soma = soma + nota
    n = n + 1
media = soma/num
print(f"{media}")