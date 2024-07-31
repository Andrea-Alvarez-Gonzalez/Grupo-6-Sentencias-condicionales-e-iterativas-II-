#Librerias
import sys

#Diccionario de meses con sus valores
ventas = {
"Enero": 15000,
"Febrero": 22000,
"Marzo": 12000,
"Abril": 17000,
"Mayo": 81000,
"Junio": 13000,
"Julio": 21000,
"Agosto": 41200,
"Septiembre": 25000,
"Octubre": 21500,
"Noviembre": 91000,
"Diciembre": 21000,
}

buscar = int(sys.argv[1])

#Realizamos el ciclo para imprimir los valores de acuerdo al umbral que necesitamos.
mayor_a = {}
for mes, valor in ventas.items():
    if valor >= buscar:
        mayor_a[mes] = valor
print(mayor_a)
