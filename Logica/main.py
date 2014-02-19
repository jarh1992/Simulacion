__author__ = 'EDGES'

from Generadores.Congruencial_Mixto import Congruencial_Mixto
from Generadores.Congruencial_Multiplicativo import Congruencial_Multiplicativo
from Generadores.Congruencial_Cuadratico import Congruencial_Cuadratico
from Generadores.Fibonacci import Fibonacci
from Generadores.MitchellMoore import MitchellMoore
from Generadores.Green import Green
import random
if __name__ == "__main__":


  r= MitchellMoore(21,48)
 # r= Fibonacci(2,23,13)
  while(not r.Periodo() ):
      print r.Generar()




