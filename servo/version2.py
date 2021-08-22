import RPi.GPIO as GPIO
import time

servoPIN = 4
GPIO.setmode(GPIO.BCM)
GPIO.setup(servoPIN, GPIO.OUT)

p = GPIO.PWM(servoPIN, 50) # GPIO 17 for PWM with 50Hz
p.start(2.5) # Initialization
print("DutyCycle : 2.5 and angle 0")
try:
  while True:
    
    x = input("")
    p.ChangeDutyCycle(5)
    print("DutyCycle : 5 and angle 45")
    #time.sleep(0.5)


    
    x = input("")
    p.ChangeDutyCycle(2.5)
    print("DutyCycle :2.5 and angle 0")
   # time.sleep(0.5)

except KeyboardInterrupt:
  p.stop()
  GPIO.cleanup()
