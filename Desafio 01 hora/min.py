hora1 = int(input("hora 1: "))
min1 = int(input("minuto 1: "))
hora2 = int(input("hora 2: "))
min2 = int(input("minuto 2: "))

minuto_excedente = (min1 + min2) //60
minuto= (min1+min2) % 60
hora = hora1 + hora2 + minuto_excedente - 24
if hora < 0:
    hora = hora * -1
if hora > 12:
    hora = hora - 12
print(f"entrada 1: {hora1}:{min1}")
print(f"entrada 2: {hora2}:{min2}")
print(f"saída: {hora}:{minuto}")
