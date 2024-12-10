#crea un diccionario llamado calificaciones, donde las claves sean los nombres de los estudiantes y los valores sean las calificaciones 
#los datos deben ser dados por el usuario
#calcular el promedio de las notas

calificaciones = {}

while True:
    print("1. Añadir estudiante y su calificación")
    print("2. Ver lista de estudiantes")
    print("3. Ver promedio de notas")
    print("4. Salir")
    opcion = int(input("Seleccione una de las opciones anteriores digitando el numero correspondiente:  "))
    if opcion == 1:
        nombre = input("Escriba el nombre del estudiante:  ")
        nota = float(input("Digite la calificación obtenida:  "))
        calificaciones [nombre] = nota
    elif opcion == 2:
        for i , j in calificaciones.items():
            print("  ")
            print(i, "la calificacion es: ", j)
            print("  ")
    elif opcion == 3:
        if calificaciones:
            promedio_notas = sum(calificaciones.values()) / len(calificaciones)
            print("  ")
            print(f"El promedio de las calificaciones dadas es de: {promedio_notas:.2f}")   
            print("  ")
        else: 
            print("  ")
            print("No hay notas para realizar el cálculo")
            print("  ")
    elif opcion == 4:
        break