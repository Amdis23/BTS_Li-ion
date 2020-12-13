import serial
import csv

myFile = open('csvexample.csv', 'w') 
writer = csv.writer(myFile)

myFile.write("Voltage,Current,Humidity,Temperature")
myFile.write("\n")

ser = serial.Serial('/dev/ttyACM0',9600)
i = 0
v = 0
i = 0
h = 0
temp = 0
soc = 1
R0 = 0
Rp = 0
Cp = 0
while True:
    measure = []
    read_serial=ser.readline()
    print read_serial
    read_serial = read_serial.split()
    var = read_serial[0]
    
    if var == "Voltage":
        print "I am here"
        v = float(read_serial[2])
        print "Voltage is"
    elif var == "Current":
        i = float(read_serial[2])
        print "Current is"
    elif var == "Temperature":
        temp = float(read_serial[2])
        print "Temperature is"  
    elif var == "Humidity":
        h = float(read_serial[2])
        print "Humidity is"
    
    else:
        print "Error!"
        
    if i != 0:
        R0 = v/(i*282.3741)
        Rp = v/(i*439.0380)
        Cp = (v*temp)/(i*219.6173)
    soc = soc - 0.0036
    
    with open('eggs.csv', 'a') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
        measure.append(v)
        measure.append(i)
        measure.append(temp)
        measure.append(h)
        measure.append(R0)
        measure.append(Rp)
        measure.append(Cp)
        measure.append(soc)
        
        spamwriter.writerow(measure)



