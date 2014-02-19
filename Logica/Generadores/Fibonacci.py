__author__ = 'EDGES'

import random
class Fibonacci:

    def __init__(self,semilla,x0,modulo):
        self.semilla= semilla
        self.modulo= modulo
        self.periodo=0
        self.x0=x0
        self.x1=None

    def Formula(self,valor,valor2):
        return (valor+ valor2)%self.modulo

    def Periodo(self):
        if(self.periodo>=self.modulo**2):
            return True
        else:
            return False

    def Generar(self):
        if(self.periodo==0):
            self.periodo+= 1
            self.x1=self.Formula(self.x0,self.semilla)
            self.x0= self.x0 if(self.x0>self.semilla) else self.semilla  
            
            return self.x1
        
        else:
            
            valor= self.x1
            self.x1=self.Formula(self.x1,self.x0)
            self.x0=valor
            self.periodo+= 1
            return self.x1





