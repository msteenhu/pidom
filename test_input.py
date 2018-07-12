#import the GPIO and time package
import RPi.GPIO as GPIO
import time

def button_callback(channel):
    print "Button pressed!"


GPIO.setmode(GPIO.BOARD)

GPIO.setup(7, GPIO.IN, pull_up_down=GPIO.PUD_UP)

GPIO.add_event_detect(7, GPIO.BOTH, callback=button_callback)

time.sleep(3600)
