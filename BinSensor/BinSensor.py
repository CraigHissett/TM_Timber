# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO
import time
from lcd import *
from Email import *

GPIO.setmode(GPIO.BOARD)

#Switch for Bin 1 to be connected to pin 16 and 3.3v pin
#Switch for Bin 2 to be connected to pin 18 and 3.3v pin
GPIO.setup(16, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(18, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)

lcd_string("Bin Sensor Alerts",LCD_LINE_1)

#This function will run when the button is triggered
def Email1(self):
        #print ('Button Triggered - Bin 1 full!')
        lcd_string('Bin #1 FULL',LCD_LINE_2)
        SendEmail("craighissett@gmail.com", 'BIN 1 FULL - PLEASE COLLECT', "")
        #print ('Trigger 10min delay')
        time.sleep(10)
        lcd_string('Bin #2 Filling',LCD_LINE_2)
        time.sleep(10)
        
def Email2(self):
        lcd_string('Bin #2 FULL',LCD_LINE_2)
        SendEmail("craighissett@gmail.com", 'BIN 2 FULL - PLEASE COLLECT', "")
        time.sleep(10)
        lcd_string('Bin #1 Filling',LCD_LINE_2)
        time.sleep(10)

GPIO.add_event_detect(16, GPIO.RISING, callback=Email1, bouncetime=300)
GPIO.add_event_detect(18, GPIO.RISING, callback=Email2, bouncetime=300)

while True:
        #print('Looping')
        lcd_string("LAN: " + get_ip_address('eth0'),LCD_LINE_3)
        lcd_string("WLAN: " + get_ip_address('wlan0'),LCD_LINE_4) 
        time.sleep(5)

GPIO.cleanup()
