import schedule
import time
import datetime
#import paho.mqtt.client as mqtt
 
print("START : %s" % time.ctime() )
 



n = 0
wartosc = 0
znacznik = 0 
temperatura1 =[18,18,18,18,18,18,18.1,18,18,18,18.1,18.1,18.1,18.1,18.1,18.1,21.1,21.1,21.1,21.1,21.1,21.1,21.1,21,21]
 
plik = open('temperatura.txt','r')
 
 
dzis_jest = datetime.datetime.now()
print "Dzis jest: ", dzis_jest.strftime("%A"), '\n' 
if dzis_jest.strftime("%A") == "Monday":
    dzien_tygodnia = "poniedzialek"
elif dzis_jest.strftime("%A") == "Tuesday":
        dzien_tygodnia = "wtorek"
elif dzis_jest.strftime("%A") == "Wednesday":
         dzien_tygodnia = "sroda\n"
elif dzis_jest.strftime("%A") == "Thursday":
         dzien_tygodnia = "czwartek\n"

 
print "Dzien tygodnia:", dzien_tygodnia, '\n'

for wiersz in plik:
#    print wiersz,
    if znacznik == 1:
        if wiersz != "\n":
	   wartosc = int(wiersz)
           temperatura1[n] = wartosc	
           n = n+1

    if wiersz == dzien_tygodnia:
        print "******************************************", '\n'
	znacznik = 1

plik.close()
 
print (temperatura1)

