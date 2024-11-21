nomes = [" "]*5
senhas = [" "]*5
tam = len(nomes)
for i in range(tam):
    nomes[i] = input("Digite os nomes: ")
    senhas[i] = input("Digite os senhas: ")
for x in range(tam):
    print(nomes[x], senhas[x], x)
