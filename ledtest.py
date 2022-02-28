# blink LED
import RPi.GPIO as GPIO
import time
# to use raspberry PI GPIO numbers
GPIO.setmode (GPIO.BCM) # GPI018
# blinking funtion
def blink (pin):
  #setup GPIO output channel
  GPIO.setup (pin, GPIO.OUT)
  GPIO.output (pin, 1)
  time.sleep (0.5)
  GPIO.output (pin, 0)
  time.sleep (0.5)

#main program blink GPIO18 (pinl12) 10 times
for i in range (0,10):
    blink(18)

#cleanup
GPIO.cleanup ()
print("program executed")