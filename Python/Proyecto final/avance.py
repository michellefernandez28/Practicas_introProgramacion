#primero el usuario y contraseña para que pueda acceder al sistema

datos_ingreso = ["abc" , 123]
numeroIntentos = 1

#usuario1 = 123
#contraseña1 = 465

for numeroIntentos in range (1,4):
    usuario = input("Ingrese el nombre de usuario:  ")
    contraseña = input ("Digite su contraseña:  ")
    if usuario != datos_ingreso[0] or contraseña != datos_ingreso[1]:
        print("**Datos de ingreso incorrecto, intentelo de nuevo**")
        print(f"Número de intento: {numeroIntentos+1}")
        
        if numeroIntentos == 3:
            print("\nLo sentimos, ha alcanzado la cantidad máxima de intentos")
            print("*****EL SISTEMA SE HA BLOQUEADO*****")
            
        else: 
            print("\n*****BIENVENIDO AL SISTEMA*****")
            transacciones = []
            presupuesto_mensual = {}
            ahorro_automatico = 0.30  # 30% de ahorro automático


            def agregar_ingreso():
                descripcion = input("Descripción del ingreso: ")
                monto = float(input("Monto del ingreso: "))
                transacciones.append({"tipo": "ingreso", "descripcion": descripcion, "monto": monto})
            def agregar_gasto():
                descripcion = input("Descripción del gasto: ")
                monto = float(input("Monto del gasto: "))
                categoria = input("Categoría del gasto (ej. alimentación, transporte): ")
                transacciones.append({"tipo": "gasto", "descripcion": descripcion, "monto": monto, "categoria": categoria})

            def establecer_presupuesto():
                categoria = input("Categoría para asignar presupuesto: ")
                monto = float(input(f"Presupuesto para {categoria}: "))
                presupuesto_mensual[categoria] = monto

            def mostrar_resumen():
                    total_ingresos = sum(t["monto"] for t in transacciones if t["tipo"] == "ingreso")
                    total_gastos = sum(t["monto"] for t in transacciones if t["tipo"] == "gasto")
                    ahorro = total_ingresos * ahorro_automatico
                    print("\n--- Resumen Financiero ---")
                    print(f"Total Ingresos: {total_ingresos}")
                    print(f"Total Gastos: {total_gastos}")
                    print(f"Ahorro Automático (30%): {ahorro}")
                    print(f"Balance: {total_ingresos - total_gastos - ahorro}\n")

            def historial_transacciones():
                print("\n--- Historial de Transacciones ---")
                for t in transacciones:
                    print(f"{t['tipo'].capitalize()}: {t['descripcion']} - Monto: {t['monto']}")
                print()

            def alertas_presupuesto():
                for categoria, presupuesto in presupuesto_mensual.items():
                    gastos_categoria = sum(t["monto"] for t in transacciones if t["tipo"] == "gasto" and t.get("categoria") == categoria)
                    if gastos_categoria > presupuesto:
                            print(f"Alerta: Has excedido el presupuesto de {categoria} por {gastos_categoria - presupuesto} unidades.")

            def menu():
                while True:
                    print("****MENÚ PRINCIPAL****")
                    print("1. Agregar Ingreso")
                    print("2. Agregar Gasto")
                    print("3. Establecer Presupuesto")
                    print("4. Mostrar Resumen Financiero")
                    print("5. Historial de Transacciones")
                    print("6. Alertas de Presupuesto")
                    print("7. Salir")
                    opcion = input("Selecciona una opción: ")
                    
                    if opcion == "1":
                        agregar_ingreso()
                    elif opcion == "2":
                        agregar_gasto()
                    elif opcion == "3":
                        establecer_presupuesto()
                    elif opcion == "4":
                            mostrar_resumen()
                    elif opcion == "5":
                            historial_transacciones()
                    elif opcion == "6":
                        alertas_presupuesto()
                    elif opcion == "7":
                        break
                    else:
                        print("Opción no válida, intenta de nuevo.")


            menu()

                

            


