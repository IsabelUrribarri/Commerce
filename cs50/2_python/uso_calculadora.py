#from calculadora import *
import calculadora

calc = calculadora.Calculadora()
data = [20,15,10,14]
#promedio = sum(data)/len(data)
promedio = calc.promedio(data)
print(promedio)