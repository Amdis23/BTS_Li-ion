#include<Wire.h>
#include<LCD.h>
#include<LiquidCrystal_I2C.h>
int Value;
const float vpp = 0.00488758553;
float Voltage=0,SOC=0;

LiquidCrystal_I2C lcd(0x27,2,1,0,4,5,6,7);
void setup() {
Serial.begin(9600);
lcd.begin (20,4);
lcd.setBacklightPin(3,POSITIVE);
lcd.setBacklight(HIGH);
  
  

}

void loop() {
Value = analogRead(A0);
Voltage=(Value * vpp);
//Voltage = (Value / 113.67);
SOC = ((Voltage/9)*100);
delay(500);
lcd.clear();
lcd.print("Voltage = ");
lcd.print(Voltage);
lcd.print("V");
lcd.setCursor(0,1);
lcd.print("SOC = ");
lcd.print(SOC);
lcd.print("%");
}
