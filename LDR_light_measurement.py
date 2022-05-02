#Add Capacitor to make it work
#event input /home/pi
import RPi.GPIO as GPIO
import time
GPIO.cleanup()
#to use raspberry PI board GPIO 18 input
GPIO.setmode(GPIO.BCM)

while True:
    GPIO.setup(18, GPIO.OUT)
    GPIO.output(18) == 0
    time.sleep(0.1)

    GPIO.setup(18, GPIO.IN)
    start_time = time.time()
    while (GPIO.input(18) == 0):
        pass
    stop_time = time.time()
    interval = start_time - start_time
    print(interval)