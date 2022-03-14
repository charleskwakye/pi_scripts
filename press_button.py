#event input /home/pi
import RPi.GPIO as GPIO
import time
GPIO.cleanup()
#to use raspberry PI board GPIO 17 input
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.IN) # GPIO 17 input
GPIO.setup(18, GPIO.OUT) # GPIO 18 output

# loop forever or ctrl + C

while True:
    if (GPIO.input(17) == 0): # input low active
        print("button pressed")
        GPIO.output(18, 1)
        time.sleep(0.3) # anti bouncing
    else:
        GPIO.output(18, 0)
        print("button release")
        time.sleep(0.3) # anti bouncing