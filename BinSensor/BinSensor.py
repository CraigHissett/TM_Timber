import RPi.GPIO as GPIO
import time
import Email

GPIO.setmode(GPIO.BOARD)

#Switch for Bin 1 to be connected to pin 16 and 3.3v pin
#Switch for Bin 2 to be connected to pin 18 and 3.3v pin
GPIO.setup(16, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(18, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)

#This function will run when the button is triggered
def EmailFunction(BinNo):
  print(“Button Triggered - Bin is full!”)
  SendEmail("craighissett@gmail.com", 'Bin ' + str(BinNo) + ' is full', "Please proceed")
  print("Trigger 10min delay")
  time.sleep(10)
  
GPIO.add_event_detect(16, GPIO.RISING, callback=EmailFunction(1), bouncetime=300)
GPIO.add_event_detect(18, GPIO.RISING, callback=EmailFunction(2), bouncetime=300)
GPIO.cleanup()
