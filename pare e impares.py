import random

ContPares = 0
ContImpares = 0
ContNumeros = 0

while(True):
    ContNumeros = int(input("ingresar cantidad de numeros a trabajar"))
    if (ContNumeros > 1 and ContNumeros <= 2):
        break
    
    for interacciones in range(ContNumeros):
        NroAlAzar = random.randint(1, 201)
        print(NroAlAzar)
        
        if (NroAlAzar % 2 == 0):
            ContPares = ContPares + 1
        else:
            ContImpares = ContImpares + 1

print ()
print ()