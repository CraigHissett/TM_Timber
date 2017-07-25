# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO
import time
from Email import*

GPIO.setmode(GPIO.BOARD)

#Switch for Bin 1 to be connected to pin 16 and 3.3v pin
#Switch for Bin 2 to be connected to pin 18 and 3.3v pin
GPIO.setup(16, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(18, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)

#This function will run when the button is triggered
def Email1():
        print ('Button Triggered - Bin 1 full!')
        SendEmail("craighissett@gmail.com", 'BIN 1 FULL - PLEASE COLLECT', "")
        print ('Trigger 10min delay')
        time.sleep(10)

def Email2():
        print ('Button Triggered - Bin 2 full!')
        SendEmail("craighissett@gmail.com", 'BIN 2 FULL - PLEASE COLLECT', "")
        print ('Trigger 10min delay')
        time.sleep(10)

GPIO.add_event_detect(16, GPIO.RISING, callback=Email1, bouncetime=300)
GPIO.add_event_detect(18, GPIO.RISING, callback=Email2, bouncetime=300)

GPIO.cleanup()
