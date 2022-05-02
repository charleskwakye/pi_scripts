from datetime import datetime
import RPi.GPIO as GPIO
import time

GPIO.cleanup()
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(18,GPIO.IN)

while True:
    GPIO.input(17) == 1
    time.sleep(0.001)
    GPIO.input(17) == 0
    print("start")
    while GPIO.input(18) == 0:
        pass
    start = datetime.now()
    print(start)
    while GPIO.input(18) == 1:
        #print(GPIO.input(18))
        pass
    end = datetime.now()
    my_time = end - start
    print(my_time.total_seconds())

    #print(start)