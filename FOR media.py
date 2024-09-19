soma = 0
num = int(input(f"digite o número de alunos: "))
for x in range (1,num+1):
    nota = float(input("informe as notas dos alunos: "))
    soma = soma + nota
media = soma/num
print(f"{media}")