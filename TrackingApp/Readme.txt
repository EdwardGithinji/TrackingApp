I Edward Githinji authored this app. With the exception of the serial_ports() function in the views.py file of the 
TrackingApp and the css styling,all other work is my original work to the best of my knowledge.

Before running this app;
On Django TrackingApp
1. Make sure the serial monitor of the arduino is not active while running this program.
2. Neither should any other program such as putty,idle,sublime etc. be using the serial com port arduino is connected to.
3. In the TrackingApp TrackingLogs.py file, change the directory of the written csv file to your desired directory and run it.
4. This directory should also be reflected in the TrackingApp views.py track() and trackdict() functions.

On arduino;
I used GPS module Neo-6M GPS and Atmega2560 arduino board. 
1. The GPS module is powered with a Vcc of 5V
2. Its RX is connected to D16(TX2) of the Atmega2560
3. Its TX is connected to D17(RX2) of the Atmega2560
4. Its ground is connected to the ground of the Atmega2560
5. Then upload the arduino code GPS_COORDSSerial.ino to the arduino board.