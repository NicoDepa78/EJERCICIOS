# Horno Nicolas Depaoli
import random
import time
import statistics
# Horno Minimo 100°C, Maximo 200°C
#Tolerancian Entre Temp Min y Max +-2°C

Temp = 0



#1 generar temp al azar
Temp = random.randint (98, 202)
print (Temp)

#  2 Solicitar ingreso por consola
while(True):
    Temp = int (input ("Ingresar Temperatura de prueba") )
    if (Temp > 98 and Temp < 201 ):
        break

Lecturas= 0
 #  Generar 10 Lecturas
for Temp in range (10):
        print(random.randint(98,201))
        Lecturas = Lecturas + random.randint(98,201)
print (str (Lecturas+Temp))
print (str (Lecturas/10))

TempMax=150
TempMin=120

if (TempMax <= Lecturas/10 ):
    print ("Temp horno Alta, apagar ")
elif (TempMax <= Lecturas/10 ):
    print ("horno estable")
elif (TempMin < Lecturas/10 ):
    print ("horno frio, encender quemador")

        
        
        
    
 