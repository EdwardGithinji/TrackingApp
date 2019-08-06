#include <TinyGPS.h>

//Serial2 -> pins(17,16)->gps pins

TinyGPS gps;
char data;
String var="";
void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600); 
  Serial2.begin(9600);
  Serial.println("Hi!, I am Arduino");
}

void loop() {
  // put your main code here, to run repeatedly:
  while(Serial.available()){    
    data = Serial.read();
    var+=data;
  }
  if(var=="TRACK"){
   gps_sms(); 
  }
  delay(10);

}

void gps_sms()
{
  bool newData = false;

  // For one second we parse GPS data and report some key values
  for (unsigned long start = millis(); millis() - start < 1000;)
  {
    while (Serial2.available())
    {
      char c = Serial2.read();
      //Serial.print(c);
      if (gps.encode(c)) 
        newData = true;  
    }
  }

  if (newData)      //If newData is true
  {
    float flat, flon,latitude,longitude;
    unsigned long age;
    gps.f_get_position(&flat, &flon, &age);   

    Serial.print("https://www.google.com/maps/?q=");
    latitude=flat == TinyGPS::GPS_INVALID_F_ANGLE ? 0.0 : flat, 6;
    Serial.print(latitude,6);
    Serial.print(",");
    longitude=flon == TinyGPS::GPS_INVALID_F_ANGLE ? 0.0 : flon, 6;
    Serial.print(longitude,6);
    delay(200);
    Serial.println((char)26); // End AT command with a ^Z, ASCII code 26
    delay(200);
    Serial.println();
    delay(2000);

  }
 
}


void initPyserial() {
  // put your main code here, to run repeatedly:

  while(Serial.available()){    
    data = Serial.read();
    var+=data;
  }
  delay(10);
}
