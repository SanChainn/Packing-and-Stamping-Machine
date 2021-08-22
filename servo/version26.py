import RPi.GPIO as GPIO
import time

servoPIN = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(servoPIN, GPIO.OUT)

p = GPIO.PWM(servoPIN, 50) # GPIO 17 for PWM with 50Hz
p.start(7.5) # Initialization
print("DutyCycle : 7.5 and angle 90")
try:
  while True:
    
    #x = input("")
    p.ChangeDutyCycle(5.5)
    print("DutyCycle : 5.5 and angle 55")
    time.sleep(0.1)
   
    #x = input("")
    p.ChangeDutyCycle(7.5)
    print("DutyCycle : 7.5 and angle 90")
    time.sleep(0.1)

    time.sleep(3)    
except KeyboardInterrupt:
  p.stop()
  GPIO.cleanup()
