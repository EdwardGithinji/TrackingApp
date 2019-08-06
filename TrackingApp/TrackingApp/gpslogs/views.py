from django.shortcuts import render
import sys
import glob
import serial
import time
import csv

#Function serial_ports() checks for active com ports on the local machine
def serial_ports():
    """ Lists serial port names

        :raises EnvironmentError:
            On unsupported or unknown platforms
        :returns:
            A list of the serial ports available on the system
    """
    if sys.platform.startswith('win'):
        ports = ['COM%s' % (i + 1) for i in range(256)]
    elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
        # this excludes your current terminal "/dev/tty"
        ports = glob.glob('/dev/tty[A-Za-z]*')
    elif sys.platform.startswith('darwin'):
        ports = glob.glob('/dev/tty.*')
    else:
        raise EnvironmentError('Unsupported platform')

    result = []
    for port in ports:
        try:
            s = serial.Serial(port)
            s.close()
            result.append(port)
        except (OSError, serial.SerialException):
            pass
    return result

def gettrack(request):
    if len(serial_ports()) >= 1:
        if request.method == 'GET':
            track()
        return render(request,'gpslogs/home.html')
    else:
        return render(request,'gpslogs/home1.html')

def posttrack(request):
    context={'posts':trackdict()}
    return render(request, 'gpslogs/trackerdata.html',context)

#trackdict() is a function to sort through the csv file returning a list of dictionaries.
def trackdict():
    Command = []
    Coords = []
    ltime = []
    with open('F:/stuff/Python/Django Projects/TrackingApp/TrackingApp/gpslogs/TrackingInfo.csv', 'r') as csvfile:
        #replace the directory above with where you have saved your csv file
        reader = csv.reader(csvfile)
        for row in reader:
            if len(row) > 1:
                #print(row)
                Command.append(row[0])
                Coords.append(row[1])
                ltime.append(row[2])
                # print(row[1])
                # print(''.join(row))
    d = {'RCommand': 0, 'RCoords': 0, 'Rltime': 0}
    L = []  #L is a list containing command, coordinate and time
    M=[] #M is a list of of all values loaded into list L during the for loop below
    for c in range(len(Command)):
        L.append(Command[c])
        L.append(Coords[c])
        L.append(ltime[c])
        M.append(L)
        L = []
    X=[]    #X will be a list containing dictionary keys and their values
    for l in range(len(M)):
        d['RCommand'] = M[l][0]
        d['RCoords'] = M[l][1]
        d['Rltime'] = M[l][2]
        X.append(d)
        d = {}
    print(X)
    return X[::-1]  #return X with the latest dictionary d appearing first

#track() is a Function to communicate with the arduino to command commencement of tracking operation and
# appending of this data to a csv file.
def track():
    for i in serial_ports():
        serial.Serial(i, 9600).close()
    active_port = serial_ports()[0]
        # serial.Serial(active_port, 9600).close()
    ArduinoSerial = serial.Serial(active_port, 9600)
    time.sleep(2)
    print(ArduinoSerial.readline())
    var='TRACK'
    ts = time.localtime()
    ArduinoSerial.write(var.encode())
    time.sleep(5)
    gpsstuff = str(ArduinoSerial.readline())[2:-9]
    print(gpsstuff)
    tsnow=time.strftime("%D %H:%M:%S", ts)
    with open('F:/stuff/Python/Django Projects/TrackingApp/TrackingApp/gpslogs/TrackingInfo.csv', 'a') as csvfile:
        # replace the directory above with where you have saved your csv file
        writer = csv.writer(csvfile)
        if len(gpsstuff) > 2:
            writer.writerow([var, gpsstuff,tsnow])
    ArduinoSerial.write(var.encode())
    time.sleep(2)
