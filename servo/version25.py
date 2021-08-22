import RPi.GPIO as GPIO
import time

servoPIN = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(servoPIN, GPIO.OUT)

p = GPIO.PWM(servoPIN, 50) # GPIO 17 for PWM with 50Hz
p.start(10.3) # Initialization
print("DutyCycle : 10.3 and angle 135")
try:
  while True:
    
    #x = input("")
    p.ChangeDutyCycle(8.2)
    print("DutyCycle : 8.2 and angle 100")
    time.sleep(0.1)
   
    #x = input("")
    p.ChangeDutyCycle(10.3)
    print("DutyCycle : 10 and angle 135")
    time.sleep(0.1)

    time.sleep(3)    
except KeyboardInterrupt:
  p.stop()
  GPIO.cleanup()
