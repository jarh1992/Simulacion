__author__ = 'EDGES'


class Congruencial_Mixto:
    def __init__(self,semilla,multiplicador,constante,modulo):
        self.semilla=semilla
        self.multiplicador=multiplicador
        self.constante= constante
        self.modulo=modulo
        self.periodo=0
        self.mensaje=""
        self.x0= None

    def Formula(self,valor):
        resultdo=(self.multiplicador*valor+self.constante)%self.modulo
        return resultdo

    def Generar(self):
        if(self.periodo==0):
            self.x0=self.Formula(self.semilla)
            self.periodo=self.periodo + 1
        else:
            self.x0=self.Formula(self.x0)
            self.periodo= self.periodo +1

        return self.x0

          
        

    def Periodo(self):
        if(self.periodo>=self.modulo or self.semilla==self.x0):
           return True
        else:
           return False

    def Validar(self):
        if(self.multiplicador%2==0):
            self.mensaje="multiplicador debe ser impar"
            return False












