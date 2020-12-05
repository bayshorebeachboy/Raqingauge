import serial
import pymysql
import time
from datetime import datetime
usbport ='/dev/cu.usbmodem14301'
ser = serial.Serial(usbport, 9600, timeout=1)
collectPluses = []
go = True
count = 0
def send_to_db(now):
    print("In Send to DB...")
    connDestination = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='', db='RivieraRain')
    curDestination = connDestination.cursor()
    sql = "INSERT INTO Pluses (pluse) VALUES (%s)"
    curDestination.execute(sql, now)
    printme = "sent " + str(now) + " to databbase"
    print("Send to DB: ", printme)
    curDestination.close()
    connDestination.commit()
    connDestination.close()

while go:
    #print("In Go...")
    RawData = ser.readline()
    #print("Raw: ",   RawData.decode('utf-8'))
    #time.sleep(1)
    #now = datetime.now()
    if RawData.decode('utf-8') != "":
        #print("Raw Data: " , RawData.decode('utf-8'))
        now = datetime.now()
        send_to_db(now)
        #print("Flushing...")
        #ser.reset_output_buffer
        #while True:
            #for line in ser.readline():
                #print(str(count) + str(': ') + chr(line) )
                #count = count+1
        
        ser.close()
        time.sleep(1)
        #print("Close...")
        ser.open()
        #print("Open...")
