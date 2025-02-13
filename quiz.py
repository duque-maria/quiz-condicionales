import math

# Quiz instrucciones condicionales
"""Dados tres números a, b y c, correspondientes a la longitud de los lados de una figura geométrica, determinar si pueden formar los lados de un triángulo."""

print("------------------------------")
print("----- VERIFICAR TRIANGULO ----")
print("------------------------------")

# input
a = int(input("Digite el primer valor: "))
b = int(input("Digite el segundo valor: "))
c = int(input("Digite el tercer valor: "))

# processing
if a + b > c:
    r= "Si pueden formar los lados de un triángulo"
if a + c > b:
    r= "Si pueden formar los lados de un triángulo"
if b + c > a:
    r= "Si pueden formar los lados de un triángulo"
else:
     r= "No se puede formar un triángulo"

# output
print("························")
print ("La respuesta es que: " + str(r))