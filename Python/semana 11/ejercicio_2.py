#Crea un programa que registre la asistencia de un grupo de estudiantes.

asistencia = [] 
def registrar_asistencia (nombre , estado):
    asistencia.append([nombre , estado])
    
def mostrar_asistencia (asistencia):
    print("\n*****Lista de asistencia:***** ")
    print("\nEstudiantes presentes: ") 
    
    Presente = (nombre for nombre, estado in asistencia if estado == "P")
    Ausente = (nombre for nombre, estado in asistencia if estado == "A")
    
    for estudiante in Presente:
        print (estudiante)
    
    print ("\nEstudiantes ausentes: ")
    for estudiantes in Ausente:
        print (estudiantes)
    
    
    ##esto pasa sacar el porcentaje
    lista_clase = len(asistencia)
    if lista_clase > 0:
        porcentaje = (len(Presente) / lista_clase) * 100
        print (f"\nEl porccentaje de asistencia a clases es de: {porcentaje: .2f}%")
        



while True:
    nombre = input("Ingrese el nombre de la persona estudiante o escriba Salir para cerrar el programa:_____")
    if nombre.lower() == "salir":  #le pongo el .lower porque si lo escriben diferente no se sale
        break

    estado = input("Escriba la letra P si la persona está presente, de lo contrario escriba la letra A:___").upper
    
    if estado in ("P" , "A"):
        registrar_asistencia(nombre , estado)
    else:
        print("Lo sentimos, solo se permite las letras P o A, intente de nuevo")
            
mostrar_asistencia(asistencia)


    


