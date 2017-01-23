

import schedule
import time
import datetime
#import paho.mqtt.client as mqtt
 
print("START : %s" % time.ctime() )
 
 
 
#print str(now)
 
#print now.strftime("%A")
 
#if now.strftime("%A") == "Wednesday":
#   print("to jest sroda")
 
 
#a = now.day
 
#print(a)
 
 
temperatura1 =[18,18,18,18,18,18,18.1,18,18,18,18.1,18.1,18.1,18.1,18.1,18.1,21.1,21.1,21.1,21.1,21.1,21.1,21.1,21,21]
 
plik = open('temperatura.txt','r')
 
 
dzis_jest = datetime.datetime.now()
print("Dzis jest: ", dzis_jest.strftime("%A")) 
if dzis_jest.strftime("%A") == "Monday":
    dzien_tygodnia = "poniedzialek"
elif dzis_jest.strftime("%A") == "Tuesday":
        dzien_tygodnia = "wtorek"
elif dzis_jest.strftime("%A") == "Wednesday":
            dzien_tygodnia = "sroda"
elif dzis_jest.strftime("%A") == "Thursday":
		dzien_tygodnia = "czwartek"

 
print("dzien tygodnia", dzien_tygodnia)
n = 0
wartosc = 0
for wiersz in plik:
    print wiersz,
    if wiersz == "sroda\n":
        print("******************************************")
        if wiersz != "\n":
            wartosc = int(wiersz)
            temperatura1[n] = wartosc
        print ("temp: ", temperatura1)
    n = n+1
plik.close()
 
print (temperatura1)
 
 
 
#for s in zrodlo:
#   print(s)
#zrodlo.close()
 
 
 
#client = mqtt.Client()
#client.username_pw_set("greg", "kaczorek")
#client.connect("localhost",1883,60)
 
 
temperatura =[18,18,18,18,18,18,18.1,18,18,18,18.1,18.1,18.1,18.1,18.1,18.1,21.1,21.1,21.1,21.1,21.1,21.1,21.1,21,21,21,21,21,21,21.1,21,21,21,21.1,21.1,21.1,21.1,21.1,21.1,21.1,22.5,22.5,22.5,22.5,20.5,20.5,20,20,20,20,20,20,20.5,20,20,20,20.5,20.5,20.5,20.5,20.5,20.5,20.5,20.5,20.5,20.5,20.5,22.5,22.5,21,21,21,21,21,22,22.5,23,23,23,22.5,22.5,22.5,22.5,22.5,17.5,17.5,17.5,17.5,17.5,17.5,17.5,17.5,17.3,18.2,15.4,10.7]
#00,01,02,03,04,05,0006,07,08,09,0010,0011,0012,0013,0014,0015,0016,0017,0018,0019,0020,0021,0022,23,24,25,26,27,28,0029,30,31,32,0033,0034,0035,0036,0037,0038,0039,0040,0041,0042,0043,0044,0045,45,47,48,49,50,51,0052,53,54,55,0056,0057,0058,0059,0060,0061,0062,0063,0064,0065,0066,0067,0068,69,70,71,72,73,74,0075,76,77,78,0079,0080,0081,0082,0083,0084,0085,0086,0087,0088,0089,0090,0091,0092,0093,0094,0095
histereza = 0.5
 
 
#print (temperatura)
 
def job(kwadrans):
    print("Data : %s" % time.ctime() )
    print("Kwadrans: ", kwadrans)
    dolna_granica = temperatura[kwadrans] - histereza
    print("Dolna Granica: ", dolna_granica)
    gorna_granica = temperatura[kwadrans] + histereza
    print("Gorna Granica: ", gorna_granica)
#    client.username_pw_set("greg", "kaczorek")  
#    client.connect("localhost",1883,60)
    time.sleep(1)
    #client.publish("topic/test", "Hello world!")
#    client.publish("/dolna/O", dolna_granica)
    time.sleep(1)
#    client.publish("/gorna/O", gorna_granica)
    time.sleep(1)
#    client.disconnect() 
 
#job
#time.sleep(10)
 
 
 
#schedule.every(1).minutes.do(job)
#schedule.every(10).seconds.do(job, kwadrans = 16)
#schedule.every().hour.do(job)
schedule.every().day.at("00:00").do(job, kwadrans = 0)
schedule.every().day.at("00:15").do(job, kwadrans = 1)
schedule.every().day.at("00:30").do(job, kwadrans = 2)
schedule.every().day.at("00:45").do(job, kwadrans = 3)
 
schedule.every().day.at("01:00").do(job, kwadrans = 4)
schedule.every().day.at("01:15").do(job, kwadrans = 5)
schedule.every().day.at("01:30").do(job, kwadrans = 6)
schedule.every().day.at("01:45").do(job, kwadrans = 7)
 
schedule.every().day.at("02:00").do(job, kwadrans = 8)
schedule.every().day.at("02:15").do(job, kwadrans = 9)
schedule.every().day.at("02:30").do(job, kwadrans = 10)
schedule.every().day.at("02:45").do(job, kwadrans = 11)
 
schedule.every().day.at("03:00").do(job, kwadrans = 12)
schedule.every().day.at("03:15").do(job, kwadrans = 13)
schedule.every().day.at("03:30").do(job, kwadrans = 14)
schedule.every().day.at("03:45").do(job, kwadrans = 15)
 
schedule.every().day.at("04:00").do(job, kwadrans = 16)
schedule.every().day.at("04:15").do(job, kwadrans = 17)
schedule.every().day.at("04:30").do(job, kwadrans = 18)
schedule.every().day.at("04:45").do(job, kwadrans = 19)
 
schedule.every().day.at("05:00").do(job, kwadrans = 20)
schedule.every().day.at("05:15").do(job, kwadrans = 21)
schedule.every().day.at("05:30").do(job, kwadrans = 22)
schedule.every().day.at("05:45").do(job, kwadrans = 23)
 
schedule.every().day.at("06:00").do(job, kwadrans = 24)
schedule.every().day.at("06:15").do(job, kwadrans = 25)
schedule.every().day.at("06:30").do(job, kwadrans = 26)
schedule.every().day.at("06:45").do(job, kwadrans = 27)
 
schedule.every().day.at("07:00").do(job, kwadrans = 28)
schedule.every().day.at("07:15").do(job, kwadrans = 29)
schedule.every().day.at("07:30").do(job, kwadrans = 30)
schedule.every().day.at("07:45").do(job, kwadrans = 31)
 
schedule.every().day.at("08:00").do(job, kwadrans = 32)
schedule.every().day.at("08:15").do(job, kwadrans = 33)
schedule.every().day.at("08:30").do(job, kwadrans = 34)
schedule.every().day.at("08:45").do(job, kwadrans = 35)
 
schedule.every().day.at("09:00").do(job, kwadrans = 36)
schedule.every().day.at("09:15").do(job, kwadrans = 37)
schedule.every().day.at("09:30").do(job, kwadrans = 38)
schedule.every().day.at("09:45").do(job, kwadrans = 39)
 
schedule.every().day.at("10:00").do(job, kwadrans = 40)
schedule.every().day.at("10:15").do(job, kwadrans = 41)
schedule.every().day.at("10:30").do(job, kwadrans = 42)
schedule.every().day.at("10:45").do(job, kwadrans = 43)
 
schedule.every().day.at("11:00").do(job, kwadrans = 44)
schedule.every().day.at("11:15").do(job, kwadrans = 45)
schedule.every().day.at("11:30").do(job, kwadrans = 46)
schedule.every().day.at("11:45").do(job, kwadrans = 47)
 
schedule.every().day.at("12:00").do(job, kwadrans = 48)
schedule.every().day.at("12:15").do(job, kwadrans = 49)
schedule.every().day.at("12:30").do(job, kwadrans = 50)
schedule.every().day.at("12:45").do(job, kwadrans = 51)
 
schedule.every().day.at("13:00").do(job, kwadrans = 52)
schedule.every().day.at("13:15").do(job, kwadrans = 53)
schedule.every().day.at("13:30").do(job, kwadrans = 54)
schedule.every().day.at("13:45").do(job, kwadrans = 55)
 
schedule.every().day.at("14:00").do(job, kwadrans = 56)
schedule.every().day.at("14:15").do(job, kwadrans = 57)
schedule.every().day.at("14:30").do(job, kwadrans = 58)
schedule.every().day.at("14:45").do(job, kwadrans = 59)
 
schedule.every().day.at("15:00").do(job, kwadrans = 60)
schedule.every().day.at("15:15").do(job, kwadrans = 61)
schedule.every().day.at("15:30").do(job, kwadrans = 62)
schedule.every().day.at("15:45").do(job, kwadrans = 63)
 
schedule.every().day.at("16:00").do(job, kwadrans = 64)
schedule.every().day.at("16:15").do(job, kwadrans = 65)
schedule.every().day.at("16:30").do(job, kwadrans = 66)
schedule.every().day.at("16:45").do(job, kwadrans = 67)
 
schedule.every().day.at("17:00").do(job, kwadrans = 68)
schedule.every().day.at("17:15").do(job, kwadrans = 69)
schedule.every().day.at("17:30").do(job, kwadrans = 70)
schedule.every().day.at("17:45").do(job, kwadrans = 71)
 
schedule.every().day.at("18:00").do(job, kwadrans = 72)
schedule.every().day.at("18:15").do(job, kwadrans = 73)
schedule.every().day.at("18:30").do(job, kwadrans = 74)
schedule.every().day.at("18:45").do(job, kwadrans = 75)
 
schedule.every().day.at("19:00").do(job, kwadrans = 76)
schedule.every().day.at("19:15").do(job, kwadrans = 77)
schedule.every().day.at("19:30").do(job, kwadrans = 78)
schedule.every().day.at("19:45").do(job, kwadrans = 79)
 
schedule.every().day.at("20:00").do(job, kwadrans = 80)
schedule.every().day.at("20:15").do(job, kwadrans = 81)
schedule.every().day.at("20:30").do(job, kwadrans = 82)
schedule.every().day.at("20:45").do(job, kwadrans = 83)
 
schedule.every().day.at("21:00").do(job, kwadrans = 84)
schedule.every().day.at("21:15").do(job, kwadrans = 85)
schedule.every().day.at("21:30").do(job, kwadrans = 86)
schedule.every().day.at("21:45").do(job, kwadrans = 87)
 
schedule.every().day.at("22:00").do(job, kwadrans = 88)
schedule.every().day.at("22:15").do(job, kwadrans = 89)
schedule.every().day.at("22:30").do(job, kwadrans = 90)
schedule.every().day.at("22:45").do(job, kwadrans = 91)
 
schedule.every().day.at("23:00").do(job, kwadrans = 92)
schedule.every().day.at("23:15").do(job, kwadrans = 93)
schedule.every().day.at("23:30").do(job, kwadrans = 94)
schedule.every().day.at("23:45").do(job, kwadrans = 95)
 
#schedule.every().monday.do(job)
#schedule.every().wednesday.at("13:15").do(job)
 
 
#schedule.run_pending()
 
while True:
    schedule.run_pending()
    time.sleep(1)
