import os


os.system("cls")


#hacer una agenda
agenda ={}

while True:
    print("1. Añadir")
    print("2. Buscar")
    print("3. Borrar")
    print("4. Mostrar")
    print("5. Salir")
    opcion = int(input("Por favor digite un valor:  "))
    if opcion == 1:
        nombre = input("digite el nombre del contacto:  ").upper()
        numero = input("Digite el número de teléfono:  ")
        agenda [nombre] = numero
        os.system("cls")
    elif opcion == 2:
        buscar = input("Escriba el nombre del contacto que desea buscar:  ").upper()
        if buscar in agenda.keys():
            print(agenda[buscar])
        else:
            print("Contacto no encontrado")
    elif opcion == 3:
        borrar = input("Escriba el nombre del contacto que desea borrar:  ")
        if borrar in agenda.keys():
            del agenda[borrar]
        os.system("cls")
    elif opcion == 4:
        for i,j in agenda.items():
            print(i, "El numero es: " , j)
    elif opcion == 5:
        break
    else:
        print("Opción incorrecta, intente de nuevo")
    
        