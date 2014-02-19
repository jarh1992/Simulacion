__author__ = 'EDGES'

import random
class MitchellMoore:
    def __init__(self,semilla,modulo):
        self.semilla=semilla
        self.modulo=modulo
        self.periodo=0
        self.mensaje=""
        self.valores= self.Inicializar()
        self.j=24
        self.k=55

    def Formula(self,valor1,valor2):
        return (valor1+valor2)%self.modulo

    def Generar(self):
        x= self.valores[len(self.valores)-self.k]
        y=self.valores[len(self.valores)-self.j]
        valor= self.Formula(x,y)
        self.j-=1
        self.k-=1
        self.periodo+=1
        if(self.j==0):
            self.j=55
        if (self.k==0):
            self.k=55
        return valor



    def Periodo(self):
        if(self.periodo>=self.modulo):
            return True
        else:
            return False


    def Inicializar(self):
        l=[]
        d=None
        for i in range(55):
            while True:
                d= random.randint(0,100)
                if(d%2!=0 or d< self.modulo):
                    break

            l.append(d)
        return l
    def Validar(self):
        if self.modulo%2==0:
            return True
        else:
            self.mensaje="modulo debe ser par"
            return False









