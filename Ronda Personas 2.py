LIMITE_CUENTA= 100
CANTIDAD_PERSONAS=10

Cuenta=0
Persona=0
SentidoGiro= "Horario"


for ciclo in range(LIMITE_CUENTA):#Control de personas dentro limite de ronda
    
    
    if (SentidoGiro == "Horario"):
        if (Persona < CANTIDAD_PERSONAS):
            Persona = Persona +1
        else:
            Persona = 1
    else:
        if (Persona >1): #sentido Antiohorario
            Persona = Persona -1
        else:   
            Persona = CANTIDAD_PERSONAS
            
    
    Cuenta +=1 #cuenta = cuenta +1 
     
     #ver de nuevo esta parte
    if (Cuenta % 8 == 0 ):#cambio de sentido de giro cuando es divisible por 8 Control de cuenta
        if (SentidoGiro == "Horario"):
            SentidoGiro = "Antihorario"
        else:
            SentidoGiro = "Horario" #Booleano uno u otro valor
            
    if (Cuenta % 11 == 0): #cambio de sentido de giro cuando es divisible por 11 Control de cuenta
        if (SentidoGiro == "Horario"):
            Persona = Persona + 1
        else:
            Persona = Persona - 1   
       
   
    print (Cuenta, Persona, SentidoGiro)