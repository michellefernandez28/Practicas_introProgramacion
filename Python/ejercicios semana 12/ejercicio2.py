#errores clasicos

numero = 5 / 0 #porque no se puede dividir entre cero

#pero yo puede hacer excepciones, o bien controlar el error para que se vea bonito
try:
    numero = 5 / 0 #porque no se puede dividir entre cero
except ZeroDivisionError:
    print("no se puede dividir por cero")
    
try:
    lista = [12]
except IndexError:
    print("error en la lista")
    
try:
    numero = int(input()) #ahi está para entero pero si ingreso un string me da error
except ValueError:
    print ("error, solo se permiten numeros")
    
#pero si quiero hacer una excepcion para todo uso esto:
try:
    123
except Exception:
    print("Intentelo de nuevo")
    