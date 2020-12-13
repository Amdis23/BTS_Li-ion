from Adafruit_CharLCD import Adafruit_CharLCD # Importing Adafruit library for LCD
from time import sleep  # Importing sleep from time library to add delay in program
# instantiate lcd and specify pins
lcd = Adafruit_CharLCD(rs=26, en=19, d4=13, d5=6, d6=5, d7=21, cols=16, lines=2)
lcd.clear()
# display text on LCD,  \n = new line
lcd.message('Welcome to\nElectronicshobbyists.com')
sleep(1)
