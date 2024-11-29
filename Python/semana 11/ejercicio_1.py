# Crea un programa que calcule el salario semanal de un empleado, teniendo en cuenta las horas trabajadas y si incluye horas extra.

# preguntar horas trabajadas y tarifa por hora

horas = int(input("Ingrese la cantidad de horas trabajadas durante esta semana"))
tarifa = float(input("Digite el monto ganado por cada hora trabajada"))

def calcular_salario (horas,tarifa):
    if horas <= 40:
        salario = horas * tarifa
    else:
        horas = horas - 40
        horas = horas * tarifa * 1.5
        salario = (40* tarifa) + (horas)
    print("El salario correspondiente a esta semana trabajada es de: ", salario)

calcular_salario(horas, tarifa)