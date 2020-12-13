import time
import Adafruit_CharLCD as LCD
import serial

# Raspberry Pi pin setup
lcd_rs = 25
lcd_en = 24
lcd_d4 = 23
lcd_d5 = 17
lcd_d6 = 18
lcd_d7 = 22
lcd_backlight = 2




# Define LCD column and row size for 16x2 LCD.
lcd_columns = 16
lcd_rows = 2


lcd = LCD.Adafruit_CharLCD(lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6, lcd_d7, lcd_columns, lcd_rows, lcd_backlight)
lcd.clear()


ser = serial.Serial('/dev/ttyACM0',9600)
i = 0
v = 0
while True:
    read_serial=ser.readline()
    print read_serial
    read_serial = read_serial.split()
    var = read_serial[0]
    lcd.cursor_pos = (1,0)
    
    if var == "Voltage":
        v = read_serial[2]
        
        lcd.message("Voltage: ")
        lcd.message(v)
        lcd.message("\n")
    elif var == "Current":
        i = read_serial[2]
        lcd.message("Current: ")
        lcd.message(i)
        lcd.message("\n")
        

