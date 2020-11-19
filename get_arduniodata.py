import serial
import pymysql
import time
from datetime import datetime
usbport ='/dev/cu.usbmodem146201'
ser = serial.Serial(usbport, 9600, timeout=1)
collectPluses = []
go = True

def send_to_db(now):
    connDestination = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='', db='RivieraRain')
    curDestination = connDestination.cursor()
    sql = "INSERT INTO Pluses (pluse) VALUES (%s)"
    curDestination.execute(sql, now)
    printme = "sent " + str(now) + " to databbase"
    print printme
    curDestination.close()
    connDestination.commit()
    connDestination.close()
    

#def makeSinglePluse():
    ##print "In make"
    ##print len(collectPluses)
    #if len(collectPluses) > 0:
        #print collectPluses
        #for i in range(0, len (collectPluses) -1):
            #print "deleting item"
            #del collectPluses[0]
            #print collectPluses
            ##printme = "send " + str(now) + " to databbase"
            ##print printme
        #if len(collectPluses) == 1:
            #send_to_db(now)
        #del collectPluses[0]
        ##print collectPluses

while go:
    RawData = ser.readline()
    now = datetime.now()
    theTime = now.strftime("%H:%M:%S")
    second = now.strftime("%S")
    if RawData <>  "":
        print RawData
        now = datetime.now()
        send_to_db(now)
        theTime = now.strftime("%H:%M:%S")
        #print RawData, theTime
        #collectPluses.append(RawData)
    ##time.sleep(5)
    ##makeSinglePluse()
    #if len(collectPluses) > 2:
        #print len(collectPluses)
        #makeSinglePluse()
    ##if len(collectPluses) == 1:
            ##send_to_db(now)
    
               


        
        