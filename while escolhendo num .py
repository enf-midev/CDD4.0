n = 1
while n ==1 :
    num = int(input("informe o número: "))
    while num <= 0:
        num = int(input("informe o número maior de 0: "))
    for x in range (1,num+1):
        print(x, end = " ")
    n = int(input(" \n Deseja digitar outro número: \n 1 para (sim) e 2 para (não): "))

