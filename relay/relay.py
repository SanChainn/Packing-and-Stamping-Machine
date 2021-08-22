from gpiozero import LED
from time import sleep

led = LED(10)

while True:
    led.on()
    print("Relay ON")
    sleep(3)
    led.off()
    print("Relay OFF")
    sleep(3)
