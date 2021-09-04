
import time


# Main
LUCES = [
	{ "nombre": "VERDE", "demora": 5 },
	{ "nombre": "AMARILLO", "demora": 2 },
	{ "nombre": "ROJO", "demora": 5 }
]
	
luzActiva = 0
while(True):
	print(LUCES[luzActiva]["nombre"])
	time.sleep(LUCES[luzActiva]["demora"])

	luzActiva += 1
	if (luzActiva == len(LUCES)):
		luzActiva = 0