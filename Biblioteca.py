def imprime_nomme(nome):
    print(f"nome: {nome}")

def imprime_num(n):
    for x in range(1,n+1,1):
        print(x, end= " ")

def somar(*numeros):
    soma = 0
    for i in numeros:
        soma= soma+i
    print(soma)

def letras(texto):
    cont = 0
    tam=len(texto)
    for x in texto:
        if x not in " !#.":
            cont+=1
    print(f"O texto sem {cont} letras.")
    for a in range(tam-1,-1,-1):
        print(texto[a], end= " ")

def listaunica(a):
    nova_lista=[]
    for x in a:
        if x not in nova_lista:
            nova_lista.append(x)
    print(nova_lista)

def primo(num):
    if (num ==1):
        return num, "não é primo"
    elif (num ==2):
        return num, "é primo"
    else:
        for x in range(2,num):
            if(num % x ==0):
                return num,"Não é primo"
        return num,"é primo"