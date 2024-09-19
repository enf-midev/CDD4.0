h1 = int(input("hora 1: "))
min1 = int(input("minuto 1: "))
h2 = int(input("hora 2: "))
min2 = int(input("minuto 2: "))

if h1 > 12:
    h1 = h1 - 12
if h2 > 12:
    h2 = h2 - 12
somahora = h1 + h2
if somahora > 12:
    somahora = somahora - 12
somamin = min1 + min2
if somamin >= 60:
    somamin = somamin - 60
    somahora = somahora + 1

print(f"{somahora}:{somamin}")
