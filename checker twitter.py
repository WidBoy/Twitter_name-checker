import requests
import platform
import os
import threading


lista = open("lista.txt", "r")
disponibles = open("disponibles-username.txt", "w")

if platform.system() == "Windows":
	os.system("cls")
	

elif platform.system() == "Linux":
	os.system("clear")

def checkear():
	for i in lista:
		i = i.strip()
		response = requests.get("https://twitter.com/" + i )

		if response.status_code == 404:
			print(i + " disponible")


			disponibles.write(i+"\n")
		
		elif response.status_code == 200:
			print(i + " no disponible")


for i in range(5):
	thread = threading.Thread(target=checkear)
	thread.start()

