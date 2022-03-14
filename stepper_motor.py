import RPi.GPIO as GPIO
import time

GPIO.cleanup ()

GPIO.setmode(GPIO.BCM)

GPIO.setup(24,GPIO.OUT)
GPIO.setup(25,GPIO.OUT)
GPIO.setup(8,GPIO.OUT)
GPIO.setup(7,GPIO.OUT)


GPIO.setwarnings(False)
sleep_time = 0.0017

while True:
    GPIO.output(24,1)
    time.sleep(sleep_time)
    GPIO.output(24,0)
    GPIO.output(25,1)
    time.sleep(sleep_time)
    GPIO.output(25,0)
    GPIO.output(8,1)
    time.sleep(sleep_time)
    GPIO.output(8,0)
    GPIO.output(7,1)
    time.sleep(sleep_time)
    GPIO.output(7,0)

