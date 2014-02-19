__author__ = 'EDGES'

import random
class Green:
    def __init__(self,semilla,modulo):
        self.semilla=semilla
        self.modulo=modulo
        self.periodo=0

        self.lista=[random.randint(0,100) for i in range(20)]


    def Formula(self,valor1,valor2):
        return (valor1+valor2)%self.modulo

    def Generar(self):
        valor= self.Formula(self.lista[len(self.lista)-18],self.lista[len(self.lista)-1])
        self.lista.append(valor)
        self.periodo+=1
        return valor;


    def Periodo(self):
        if(self.periodo>=self.modulo):
            return True
        else:
            return False


