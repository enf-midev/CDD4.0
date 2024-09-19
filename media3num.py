nota1 = float(input("receba a 1ª nota"))
nota2 = float(input("receba a 2ª nota"))
nota3 = float(input("receba a 3ª nota"))
media = (nota1+nota2+nota3)/3
if media >= 7:
    print(f"Média: {media:.1f}, Aluno APROVADO")
else:
   if media  >=4 :
       print(f"Média: {media:.1f}, Aluno em RECUPERAÇÃO")
   else:
       print(f"Média: {media:.1f}, Aluno em REPROVADO")