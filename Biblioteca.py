#self.nome = atributos/ =n: argumentos  método construtor
#todo atribuuto que tiver um valor padrãpo deve ficar por ultimo
class Pessoa():
    def __init__(self,n,p,i):
        self.nome= n
        self.peso= p
        self.idade= i
        self.comendo=False
        self.andando=False
        self.dormindo=False
    def andar(self):
        if self.comendo == False:
           if self.dormindo == False:
               if self.andando == False:
                   print(f"{self.nome}. Foi andar.")
                   self.andando = True

               else:
                   print(f"{self.nome}Já esta andando..")
           else:
               print(f"{self.nome}Não pode andar, está dormindo.")
        else:
            print(f"{self.nome} Não pode andar, está comendo.")
    def comer(self):
         if self.andando == False:
            if self.dormindo == False:
                if self.comendo == False:
                    print(f"{self.nome}. Foi comer")
                    self.comendo=True
                else:
                    print(f"Já está comendo.")
            else:
                print(f"Não pode comer, está dormindo.")
         else:
            print(f"Não pode comer, está andando.")
    def dormir(self):
        if self.andando == False:
            if self.comendo == False:
                if self.dormindo == False:
                    print(f"{self.nome}. Foi dormir")
                    self.dormindo = True
                else:
                    print(f"Já está dormindo.")
            else:
                print(f"Não pode dormir, está comendo.")
        else:
            print(f"Não pode dormir, está andando.")
    def parar_andar(self):
        if self.andando == True:
            print(f"Parou de andar.")
            self.andando = False


    def parar_comer(self):
        if self.comendo == True:
            print(f"Parou de comer.")
            self.comendo = False

    def acordando(self):
        if self.acordando == True:
            print(f"Acordou.")
            self.acordando = False




class Animal():
    def __init__(self,nome,cor):
        self.nome= nome
        self.cor= cor

    def comer(self):
        print(f"O {self.nome} está comendo..")

class Gato(Animal):
    def __init__(self,nome,cor):
        super().__init__(nome,cor)
    def miar(self):
        print(f"O {self.nome} está miando..")

class Cachorro(Animal):
    def __init__(self,nome,cor):
        super().__init__(nome,cor)
    def latir(self):
        print(f"O {self.nome} está latindo..")

class Vaca(Animal):
    def __init__(self,nome,cor):
        super().__init__(nome,cor)
    def mungir(self):
        print(f"O {self.nome} está mugindo..")

class Coelho(Animal):
    def __init__(self,nome,cor):
        super().__init__(nome,cor)
    def chia(self):
        print(f"O {self.nome} está chiando..")

