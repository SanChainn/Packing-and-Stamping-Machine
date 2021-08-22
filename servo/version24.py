import RPi.GPIO as GPIO
import time

servoPIN = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(servoPIN, GPIO.OUT)

p = GPIO.PWM(servoPIN, 50) # GPIO 17 for PWM with 50Hz
p.start(3.5) # Initialization
print("DutyCycle : 3.5 and angle 0")
try:
  while True:
    
    #x = input("")
    p.ChangeDutyCycle(2.8)
    print("DutyCycle : 4.5 and angle 55")
    time.sleep(0.5)
   
    #x = input("")
    p.ChangeDutyCycle(3.8)
    print("DutyCycle : 3.8 and angle 0")
    time.sleep(0.5)

    
except KeyboardInterrupt:
  p.stop()
  GPIO.cleanup()
