__author__ = 'EDGES'


class Congruencial_Cuadratico:
    """ este es una clase para generar numeros pseudoaleatorios con el algoritmo Congruencial_Cuadratico"""
    def __init__(self,semilla,multiplicador,multiplicador2,constante,modulo):
        self.semilla=semilla
        self.multiplicador=multiplicador
        self.multiplicador2=multiplicador2
        self.constante=constante
        self.modulo=modulo
        self.mensaje=""
        self.periodo=0
        self.x0=None
    def Formula(self,valor):
        resultdo=(self.multiplicador2*valor**2 +self.multiplicador*valor +self.constante)%self.modulo
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
       r=None
       a= self.constante
       b= self.modulo
       while(b>0):
           r=a%b
           a=b
           b=r
       if(a!=1):
           self.mensaje="constante y modulo deben ser primos relativos"
           return False
       else:
           return True




