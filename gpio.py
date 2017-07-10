#import the GPIO and time package
import RPi.GPIO as GPIO
import time



class Output:
    CHANNELS = [11,13,15,16,18,22,24]

    def __init__(self):
        GPIO.setmode(GPIO.BOARD)

        for channel in Output.CHANNELS:
            GPIO.setup(channel, GPIO.OUT)
            GPIO.output(channel, True)


    def __del__(self):
        for channel in Output.CHANNELS:
            GPIO.output(channel, True)

        GPIO.cleanup()


    def on(self, channel_id):
        GPIO.output(Output.CHANNELS[channel_id], False)
    def off(self, channel_id):
        GPIO.output(Output.CHANNELS[channel_id], True)
    def pulse(self, channel_id, duration=0.2):
        GPIO.output(Output.CHANNELS[channel_id], False)
        time.sleep(duration)
        GPIO.output(Output.CHANNELS[channel_id], True)

