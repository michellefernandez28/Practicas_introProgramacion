import os


os.system("cls")


#hacer una agenda
agenda ={}

while True:
    try:
        print("1. Añadir / Modificar")
        print("2. Buscar")
        print("3. Borrar")
        print("4. Mostrar")
        print("5. Salir")
        opcion = int(input("Por favor digite un valor:  "))
        if opcion == 1:
            nombre = input("digite el nombre del contacto:  ").upper()
            if nombre in agenda.keys():
                print("El nombre ya tiene un numero asociado y es: ", agenda[nombre])
                respuesta = input("Presione S si quiere cambiar el numero o presione cualquier otra letra si no:  ")
                if respuesta.upper() == "S":
                    numero = input("Digite el nuevo número:  ")
                    agenda[nombre] = numero
                    os.system("cls")
                else: 
                    print("Se mantuvo el numero")
                    os.system("cls")
            else:
                numero = input("Digite el número de teléfono:  ")
                agenda [nombre] = numero
                os.system("cls")
        elif opcion == 2:
            buscar = input("Escriba el nombre del contacto que desea buscar:  ").upper()
            if buscar in agenda.keys():
                print(agenda[buscar])
            else:
                print("Contacto no encontrado")
                
            for clave, valor in agenda.items():
                if clave.startswith(buscar):
                    print(clave , "tiene el telefono asociado " , valor)
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
    except Exception:
        print ("intente de nuevo")   