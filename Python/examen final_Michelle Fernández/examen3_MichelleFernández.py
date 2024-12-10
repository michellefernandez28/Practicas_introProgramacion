## hacer un programa para registrar a estudiantes en una sección X, ademas tengo que pedir contraseñas
##voy a poner el cosito para que se limpie porque no me gusta ver la terminal llena
import os
os.system("cls")


datos_ingreso = ["abc" , 123]
intentos_ingreso = 1

#abro bucle para pedir la contraseña
for intento_ingreso in range(1,4):
    usuario_solicitado = input("Ingrese el nombre de usuario:__")
    contraseña_solicitada = input("Ingrese la contraseña:___")
    if usuario_solicitado != datos_ingreso[0] or contraseña_solicitada != datos_ingreso[1]:
        print("Lo sentimos, datos de ingreso incorrecto, intentelo de nuevo")


def menu_inscripciones():
    while True:
        print("___BIENVENIDO AL MENÚ PRINCIPAL___")
        print("1. Inscripción de estudiantes")
        print("2. Consulta por sección")
        print("3. Salir")
        seleccion = input("Seleccione una de las opciones anteriores:___")
        
            
    
    
    



