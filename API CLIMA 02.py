
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
    ListaCiudades = RecuperarUrl()
    
    for index, item in enumerate(ListaCiudades):
        if (item["fid"] ==6425):
            Temperatura = item["weather"]["temp"]
            Humedad = item["weather"]["humidity"]
            Presion = item["weather"]["pressure"]
            Descripcion = item["weather"]["description"]
            Viento = item ["weather"]["wing_deg"]
            
            print("Córdoba Capital:")
            print("Temperatura:",Temperatura)
            print("Humedad:",Humedad)
            print("Presion:",Presion)
            print("Cielo:",Descripcion)
            print("Viento:",Viento)
 
 
 #main
if (__name__ == "__main__"):
    main()
    

