# Librerias
import os
import requests as req
from dotenv.main import load_dotenv
load_dotenv()

TOKEN = os.getenv("TOKEN")
ID_CHAT = os.getenv("ID_CHAT")
 
# Parámetros
URL_SMN = "https://ws.smn.gob.ar/map_items/weather"
URL_TELEGRAM = "https://api.telegram.org/bot"
TOKEN = os.getenv("TOKEN")
ENDPOINT = "sendMessage"
ID_CHAT = os.getenv("ID_CHAT")

 
 
 #funciones
def RecuperarUrl():
	consulta = req.get(URL_SMN)
	consulta.status_code
	return consulta.json()

def notificarTelegram(datos):
	# Aprovechando la macro f, vamos tomando los items del diccionario datos y formamos el texto a enviar.
	TEXTO = f"Córdoba Capital ahora:\nTemperatura: {datos['temperatura']}\nHumedad: {datos['humedad']}\nPresion: {datos['presion']}\nCielo: {datos['descripcion']}\nViento: {datos['viento']}"
	URL_MENSAJE = f"{URL_TELEGRAM}{TOKEN}/{ENDPOINT}?chat_id={ID_CHAT}&text={TEXTO}"
	consulta = req.get(URL_MENSAJE)
	
	if (consulta.status_code == 200):
		print("Notificación Telegram enviada")
    

def main():
	listaCiudades = RecuperarUrl()
	
	for index, item in enumerate(listaCiudades):
		if (item["fid"] == 6425):
			
			datos = {
            	"temperatura": item["weather"]["temp"],
            	"humedad": item["weather"]["humidity"],
            	"presion": item["weather"]["pressure"],
				"descripcion": item["weather"]["description"],
				"viento": item ["weather"]["wing_deg"]
			}
			
			
			notificarTelegram(datos)
 
 
 #main
if (__name__ == "__main__"):
    main()
