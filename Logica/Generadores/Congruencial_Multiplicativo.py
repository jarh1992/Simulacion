__author__ = 'EDGES'

class Congruencial_Multiplicativo:

    
    def __init__(self,semilla,multiplicador,modulo):
        self.semilla= semilla
        self.multiplicador= multiplicador
        self.modulo= modulo
        self.periodo=0
        self.x0= None
        
    def Formula(self,valor):
        resultado= (self.multiplicador*valor)%self.modulo
        return resultado
    

    def Generar(self):
        if(self.periodo==0):
            self.x0=self.Formula(self.semilla)
            self.periodo=self.periodo + 1
        else:
            self.x0=self.Formula(self.x0)
            self.periodo= self.periodo +1

            
    def Periodo(self):
        if(self.periodo>=self.modulo or self.semilla==self.x0):
           return True
        else:
           return False    

    def Validar(self):
        pass
