soma = 0
for x in range (1,11):
    num = int(input(f"digite o número {x} "))
    if num % 2 != 0:
        soma = soma + num
print(f"{soma}")