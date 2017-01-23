import os
import schedule
import time
import datetime
import paho.mqtt.client as mqtt

print "START PROGRAMU: %s" % time.ctime(), '\n' 

program1 = "WYLACZONY!"
# Ustawienia defaultowe
programO = "KOMFORT"
programW = "KOMFORT"
programK = "KOMFORT"



def on_connect(client, userdata, flags, rc):
  print("Connected with result code "+str(rc))
  client.subscribe("/Program/O")
  client.subscribe("/Program/W")
  client.subscribe("/Program/K")

def on_message(client, userdata, msg):
    global programO
    global programW
    global programK
    temat = str(msg.topic)

    if temat == "/Program/O":
      programO = str(msg.payload)
      if programO == "#0":
	 programO = "WYLACZONY"
      if programO == "#1":
	 programO = "KOMFORT"
      if programO == "#2":
	 programO = "NOC"
      if programO == "#3":
	 programO = "UZYTKOWNIK"

    if temat == "/Program/W":
      programW = str(msg.payload)
      if programW == "#0":
	 programW = "WYLACZONY"
      if programW == "#1":
	 programW = "KOMFORT"
      if programW == "#2":
	 programW = "NOC"
      if programW == "#3":
	 programW = "UZYTKOWNIK"


    if temat == "/Program/K":
      programK = str(msg.payload)
      if programK == "#0":
	 programK = "WYLACZONY"
      if programK == "#1":
	 programK = "KOMFORT"
      if programK == "#2":
	 programK = "NOC"
      if programK == "#3":
	 programK = "UZYTKOWNIK"



    print "Temat odczytany z MQTT:", msg.topic
    print "Program odczytany z MQTT:", msg.payload
#    client.disconnect()


client = mqtt.Client()
#client.username_pw_set("greg", "kaczorek")
#client.connect("localhost",1883,60)


client.on_connect = on_connect
client.on_message = on_message

client.loop_start()

#temperatura =[22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22]
#00,01,02,03,04,05,0006,07,08,09,0010,0011,0012,0013,0014,0015,0016,0017,0022,0019,0022,0022,0022,22,24,25,26,27,28,0029,30,31,32,0033,0034,0035,0036,0037,0038,0039,0040,0041,0042,0043,0044,0045,45,47,48,49,50,51,0052,53,54,55,0056,0057,0058,0059,0060,0061,0062,0063,0064,0065,0066,0067,0068,69,70,71,72,73,74,0075,76,77,78,0079,0080,0081,0082,0083,0084,0085,0086,0087,0088,0089,0090,0091,0092,0093,0094,0095

oliwka_temp =[22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22]
 
wika_temp =[22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22]

kuba_temp =[22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22]
  
komfort =[22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22]

noc =[18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18]

wylacz =[5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5]


 

histereza = 0.2

#  *************************  Definicje procedur ***************************************







def aktualizuj_harmonogram_z_pliku(plik_harmonogram, tablica_harmonogram, dzien_tygodnia):

    try:
	print "Start aktualizacji harmonogramu dla: ", plik_harmonogram

	n = 0
	wartosc = 0
	znacznik = 0 
#	plik = open('tempO.txt','r')
	plik = open(plik_harmonogram,'r')
	
	
#Ustala aktualny dzien tygodnia: 
	if dzien_tygodnia == "Monday":
	    dzien_tygodnia = "poniedzialek\n"
	elif dzien_tygodnia == "Tuesday":
	        dzien_tygodnia = "wtorek\n"
	elif dzien_tygodnia == "Wednesday":
	        dzien_tygodnia = "sroda\n"
	elif dzien_tygodnia == "Thursday":
	        dzien_tygodnia = "czwartek\n"
	elif dzien_tygodnia == "Friday":
 	       dzien_tygodnia = "piatek\n"
	elif dzien_tygodnia == "Saturday":
	        dzien_tygodnia = "sobota\n"
	elif dzien_tygodnia == "Sunday":
 	       dzien_tygodnia = "niedziela\n"
 
	print "Dzien tygodnia:", dzien_tygodnia, '\n'


#Po ustaleniu dnia tygodnia, wyszukuje w pliku harmonogram grzania dla tego dnia i przepisuje go do zmiennej tablicowej

	for wiersz in plik:
	#    print wiersz,
#	    print n
	    if znacznik == 1:   #znacznik = 1 oznacza ze odnaleziono dzien tygodnia w pliku i mozna zaczac odczytywac temperatury
	        if (wiersz != "\n") and (n<=95):
	#	   wartosc = int(wiersz)
		   wartosc = float(wiersz)
#	           oliwka_temp[n] = wartosc
		   tablica_harmonogram[n] = wartosc	
	           n = n+1

	    if wiersz == dzien_tygodnia:
	        print "Znaleziono dzien tygodnia w pliku", '\n'
		znacznik = 1

	plik.close()
#	print oliwka_temp

    except:
	  print "Wystapily problemy z odczytem pliku ", plik_harmonogram
	  print "Wlaczam tryb domyslny"
	  tablica_harmonogram = komfort
	  return

	




def wyslij_temp(q1, q2, q3, q4, m, tablica_harmonogram):


#	minuta = int (dzis_jest.strftime("%M"))
	minuta = int (m)
#	print "minuta z wyslij_temp:" , minuta

	if minuta >= 0 and minuta < 15:
		kwadrans = q1
	if minuta >= 15 and minuta < 30:
		kwadrans = q2
	if minuta >= 30 and minuta < 45:
		kwadrans = q3
	if minuta >= 45 and minuta <= 59:
		kwadrans = q4
	print "Data : %s" % time.ctime() 
	print "Kwadrans: ", kwadrans
#	print "Temperatura z harmonoramu:" , oliwka_temp[kwadrans]
	print "Temperatura z harmonoramu:" , tablica_harmonogram[kwadrans]
#	dolna_granica = oliwka_temp[kwadrans] - histereza
	dolna_granica = tablica_harmonogram[kwadrans] - histereza
	print "Dolna Granica: ", dolna_granica
#	gorna_granica = oliwka_temp[kwadrans] + histereza
	gorna_granica = tablica_harmonogram[kwadrans] + histereza
	print "Gorna Granica: ", gorna_granica
	print "#########################################################"
#	client.username_pw_set("greg", "kaczorek")  
#	client.connect("localhost",1883,60)
	time.sleep(0.4)
	#client.publish("topic/test", "Hello world!")
	#client.publish("/dolna/O", dolna_granica)
	time.sleep(0.4)
	#client.publish("/gorna/O", gorna_granica)
	time.sleep(0.4)
#	client.disconnect()




def ustal_godzine(g, m, tablica_harmonogram):


	 godzina = int (g)
	 minuta = m
	 if godzina == 0 :
		wyslij_temp(0,1,2,3,minuta,tablica_harmonogram)
	 if godzina == 1 :
		wyslij_temp(4,5,6,7,minuta,tablica_harmonogram)
	 if godzina == 2 :
		wyslij_temp(8,9,10,11,minuta,tablica_harmonogram)
	 if godzina == 3 :
		wyslij_temp(12,13,14,15,minuta,tablica_harmonogram)
	 if godzina == 4 :
		wyslij_temp(16,17,22,19,minuta,tablica_harmonogram)
	 if godzina == 5 :
		wyslij_temp(22,22,22,22,minuta,tablica_harmonogram)
	 if godzina == 6 :
		wyslij_temp(24,25,26,27,minuta,tablica_harmonogram)
	 if godzina == 7 :
		wyslij_temp(28,29,30,31,minuta,tablica_harmonogram)
	 if godzina == 8 :
		wyslij_temp(32,33,34,35,minuta,tablica_harmonogram)
	 if godzina == 9 :
		wyslij_temp(36,37,38,39,minuta,tablica_harmonogram)
	 if godzina == 10 :
		wyslij_temp(40,41,42,43,minuta,tablica_harmonogram)
	 if godzina == 11 :
		wyslij_temp(44,45,46,47,minuta,tablica_harmonogram)
	 if godzina == 12 :
		wyslij_temp(48,49,50,51,minuta,tablica_harmonogram)
	 if godzina == 13 :
		wyslij_temp(52,53,54,55,minuta,tablica_harmonogram)
	 if godzina == 14 :
		wyslij_temp(56,57,58,59,minuta,tablica_harmonogram)
	 if godzina == 15 :
		wyslij_temp(60,61,62,63,minuta,tablica_harmonogram)
	 if godzina == 16 :
		wyslij_temp(64,65,66,67,minuta,tablica_harmonogram)
	 if godzina == 17 :
		wyslij_temp(68,69,70,71,minuta,tablica_harmonogram)
	 if godzina == 18 :
		wyslij_temp(72,73,74,75,minuta,tablica_harmonogram)
	 if godzina == 19 :
		wyslij_temp(76,77,78,79,minuta,tablica_harmonogram)
	 if godzina == 20 :
		wyslij_temp(80,81,82,83,minuta,tablica_harmonogram)
	 if godzina == 21 :
		wyslij_temp(84,85,86,87,minuta,tablica_harmonogram)
	 if godzina == 22 :
		wyslij_temp(88,89,90,91,minuta,tablica_harmonogram)
	 if godzina == 23 :
		wyslij_temp(92,93,94,95,minuta,tablica_harmonogram)

def wszystko():
	dzis_jest = datetime.datetime.now()
	dzien_tygodnia = dzis_jest.strftime("%A")
	minuta = dzis_jest.strftime("%M")
	godzina = dzis_jest.strftime("%H")
	
	print "Dzis jest: ", dzis_jest.strftime("%A")
	print "Godzina:", dzis_jest.strftime("%H")
	print "Minuta:", dzis_jest.strftime("%M"), '\n'
	print "Program:", program	


	if programO == 'UZYTKOWNIK':
	  aktualizuj_harmonogram_z_pliku('tempO.txt', oliwka_temp, dzien_tygodnia)
	  ustal_godzine(godzina, minuta, oliwka_temp)
	if programO == 'KOMFORT':
	   ustal_godzine(godzina, minuta, komfort)

	if programO == 'NOC':
	   ustal_godzine(godzina, minuta, noc)

	if programO == 'WYLACZ':
	   ustal_godzine(godzina, minuta, wylacz)

        aktualizuj_harmonogram_z_pliku('tempW.txt', wika_temp, dzien_tygodnia)
        ustal_godzine(godzina, minuta, wika_temp)

        aktualizuj_harmonogram_z_pliku('tempK.txt', kuba_temp, dzien_tygodnia)
	ustal_godzine(godzina, minuta, kuba_temp)
	


#wszystko(program)


schedule.every(1).minutes.do(wszystko)
#schedule.every(10).seconds.do(wszystko)
#schedule.every().hour.do(job)
#schedule.every().day.at("00:00").do(job, kwadrans = 0)
#schedule.every().day.at("00:15").do(job, kwadrans = 1)
#schedule.every().day.at("00:30").do(job, kwadrans = 2)
#schedule.every().day.at("00:45").do(job, kwadrans = 3)


while True:
    schedule.run_pending()
    time.sleep(0.5)
#    client.loop_forever()



client.loop_stop()
client.disconnect()


