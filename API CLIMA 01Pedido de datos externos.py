#librerias
import requests

 
 
#URL
URL = "https://ws.smn.gob.ar/map_items/weather"
 
 
 #funciones
def RecuperarUrl():
    consulta = requests.get(URL)
    consulta.status_code
    return consulta.json()
    

def main():
    info = RecuperarUrl()
    print (info)
 
 
 #main
if (__name__ == "__main__"):
    main()
    




