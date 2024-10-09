#self.nome = atributos/ =n: argumentos  método construtor
#todo atribuuto que tiver um valor padrãpo deve ficar por ultimo
class Pessoa:
    def __init__(self,n,p,i=0,comendo=False, andando=False, dormindo=False):
        self.nome= n
        self.peso= p
        self.idade= 0
        self.comendo=comendo
        self.andando=andando
        self.dormindo=dormindo
    def andar(self):
        if self.andando == False:
            print(f"{self.nome}Foi andar.")
            self.andando=True
        else:
            print(f"{self.nome} Foi andar")
    def comer(self):
        if self.comendo == False:

            print(f"{self.nome}. Foi comer")
            self.comendo=True
        else:
            print(f"Já está comendo.")

    def dormir(self):
        if self.dormindo==False:
            print(f"{self.nome}Foi dormir")
        else:
            print(f"Já está dormindo.")

p1 = Pessoa("Milene",p=60,i=24)
p1.nome="Milene Machado"
p1.comer()
p1.comer()
