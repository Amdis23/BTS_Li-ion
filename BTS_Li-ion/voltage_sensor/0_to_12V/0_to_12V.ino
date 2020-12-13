int value = 0;
float voltage;
float R1 = 30000.0;
float R2 = 7500.0;
const int analogIn = A0;
double mVperAmp = 100; // use 100 for 20A Module and 66 for 30A Module
double RawValue= 0;
double ACSoffset = 2500; 
double Voltage = 0;
double Amps = 0;

void setup(){
  Serial.begin(9600);
}

void loop(){
  value = analogRead(A1);
  voltage = value * (5.0/1024.0);
  voltage=voltage/0.2;
  Serial.print("Voltage =");
  Serial.println(voltage);
  delay(500);
 RawValue = analogRead(analogIn);
 Voltage = (RawValue / 1024.0) * 5000; // Gets you mV
 Amps = (-(Voltage - ACSoffset) / mVperAmp);
 
 Serial.print("Amps = "); // shows the voltage measured 
 Serial.println(RawValue); // the '2' after voltage allows you to display 2 digits after decimal point
 delay(1000); 
}
