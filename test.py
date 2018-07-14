#import the GPIO and time package
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

GPIO.setup(11, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(15, GPIO.OUT)
GPIO.setup(16, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)
GPIO.setup(24, GPIO.OUT)



# loop through 50 times, on/off for 1 second
for i in range(200):
    GPIO.output(11,True)
    time.sleep(0.1)
    GPIO.output(13,True)
    time.sleep(0.1)
    GPIO.output(15,True)
    time.sleep(0.1)
    GPIO.output(16,True)
    time.sleep(0.1)
    GPIO.output(18,True)
    time.sleep(0.1)
    GPIO.output(22,True)
    time.sleep(0.1)
    GPIO.output(24,True)
    time.sleep(3)
 
    GPIO.output(11,False)
    time.sleep(0.1)
    GPIO.output(13,False)
    time.sleep(0.1)
    GPIO.output(15,False)
    time.sleep(0.1)
    GPIO.output(16,False)
    time.sleep(0.1)
    GPIO.output(18,False)
    time.sleep(0.1)
    GPIO.output(22,False)
    time.sleep(0.1)
    GPIO.output(24,False)
    time.sleep(3)
 

GPIO.cleanup()

