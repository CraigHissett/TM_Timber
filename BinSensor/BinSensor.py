# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO
import time
from lcd import *
from Email import *

lcd_init ()
GPIO.setmode(GPIO.BOARD)

#Switch for Bin 1 to be connected to pin 18 and 3.3v pin
#Switch for Bin 2 to be connected to pin 16 and 3.3v pin
GPIO.setup(16, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(18, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)

lcd_string("    Dust-O-Matic    ",LCD_LINE_1)

#This function will run when the button is triggered
def Notifier(channel):
        if channel==18:
                lcd_string('  TRAILER #1 FULL   ',LCD_LINE_2)
                SendEmail('TRAILER 1 FULL - PLEASE COLLECT', "")
                lcd_string(' TRAILER #2 Filling ',LCD_LINE_3)
        elif channel==16:
                lcd_string('  TRAILER #2 FULL   ',LCD_LINE_2)
                SendEmail('TRAILER 2 FULL - PLEASE COLLECT', "")
                lcd_string(' TRAILER #1 Filling ',LCD_LINE_3)

GPIO.add_event_detect(18, GPIO.RISING)
GPIO.add_event_detect(16, GPIO.RISING)

while True:
        #print('Looping')
        lcd_string("LAN: " + get_ip_address('eth0'),LCD_LINE_4)
        #lcd_string("WLAN: " + get_ip_address('wlan0'),LCD_LINE_4)
        if GPIO.event_detected(18):
                lcd_string('TRAILER #1 TRIGGERED',LCD_LINE_2)
                Notifier(18)
        if GPIO.event_detected(16):
                lcd_string('TRAILER #2 TRIGGERED',LCD_LINE_2)
                Notifier(16)
        time.sleep(0.5)
GPIO.cleanup()
