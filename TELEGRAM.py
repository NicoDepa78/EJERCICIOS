
import requests as req
from requests.exceptions import URLRequired 

def main():
    URL_TELEGRAM = "https://api.telegram.org/bot"
    TOKEN ="1957090271:AAH_4H5_VZYczzWKwtQC1J-3LEZX3dYlB3w"
    ENDPOINT = "sendMessage"
    ID_CHAT = "-406475613"
    TEXTO = "prueba de telegram"
    URL_MENSAJE = f"{URL_TELEGRAM}{TOKEN}/{ENDPOINT}?chat_id={ID_CHAT}&text={TEXTO}"
    consulta = req.get(URL_MENSAJE)
    
    if (consulta.status_code == 200):
	    print("Mensaje enviado")
	
if (__name__ == "__main__"):
	main()