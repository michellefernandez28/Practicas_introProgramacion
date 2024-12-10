#Crea un programa que registre la asistencia de un grupo de estudiantes.

asistencia = [] 

def registrar_asistencia (nombre , estado):
    asistencia.append((nombre , estado)) 
    
def mostrar_asistencia (asistencia):
    
    presentes = (nombre for nombre, estado in asistencia if estado == "P")
    ausente = (nombre for nombre, estado in asistencia if estado == "A")
    
    print("\n*****Lista de asistencia:***** ")
    
    print("\nEstudiantes presentes: ") 
    for estudiante in presentes:
        print (estudiante.title())
    
    print ("\nEstudiantes ausentes: ")
    for estudiantes in ausente:
        print (estudiantes.title())
    
#voy con el porcentaje
        porcentaje = int((estado in "P") / asistencia) * 100 #no se como convertir para que todos los datos sean iguales
        porcentaje
        

##el while no lo tengo que tocar más, está funcionando

while True:
   
    nombre = input("Escriba el nombre de la persona estudiante o bien 'Salir' para cerrar el programa: ")
    if nombre.lower() == "salir":
        break 
    
    estado = input("Ingrese 'P' para presente o 'A' para ausente: ").upper()
    
    if estado in ("P", "A"):
        registrar_asistencia(nombre, estado)
    else:
        print("Lo sentimos, solo se permiten las letras 'P' o 'A'. Por favor vuelva a intentarlo")
            
mostrar_asistencia(asistencia) #esto no entiendo, me tira error, pero si lo quito no me muestra nada y si le escribo un print me da error tambien
    


    


