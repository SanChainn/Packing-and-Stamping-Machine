from time import sleep
import pigpio
import RPi.GPIO as GPIO
import time

glue_sensor = 26
stamp_sensor = 19
buzzer=19

DIR = 20     # Direction GPIO Pin
STEP = 21    # Step GPIO Pin
SWITCH = 16  # GPIO pin of switch

# Connect to pigpiod daemon
pi = pigpio.pi()


# Set up pin as output GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(glue_sensor,GPIO.IN)
GPIO.setup(stamp_sensor,GPIO.IN)
GPIO.setup(buzzer,GPIO.OUT)
GPIO.output(buzzer,False)



# Set up pins as an output
pi.set_mode(DIR, pigpio.OUTPUT)
pi.set_mode(STEP, pigpio.OUTPUT)

# Set up input switch
pi.set_mode(SWITCH, pigpio.INPUT)
pi.set_pull_up_down(SWITCH, pigpio.PUD_UP)

MODE = (14, 15, 18)   # Microstep Resolution GPIO Pins
RESOLUTION = {'Full': (0, 0, 0),
              'Half': (1, 0, 0),
              '1/4': (0, 1, 0),
              '1/8': (1, 1, 0),
              '1/16': (0, 0, 1),
              '1/32': (1, 0, 1)}
for i in range(3):
    pi.write(MODE[i], RESOLUTION['1/8'][i])

# Set duty cycle and frequency
pi.set_PWM_dutycycle(STEP, 128)  # PWM 1/2 On 1/2 Off
pi.set_PWM_frequency(STEP, 500)  # 500 pulses per second

# Set stepper motor direction clockwise
pi.write(DIR,1)

try:
    while True:
        #pi.write(DIR,1)  # Set direction
	#pi.set_PWM_dutycycle(STEP,128)
	#pi.set_PWM_frequency(STEP,500)
	#sleep(5)
        #sleep(1)
	#print("FULL STEPPING ")
	#print("STOP")
	#pi.write(STEP,0)
	#sleep(2)
	if GPIO.input(glue_sensor):
		GPIO.output(buzzer,False)
		print("Glue_sensor detect no object")
		pi.set_PWM_dutycycle(STEP,128)
		pi.set_PWM_frequency(STEP,500)
	elif GPIO.input(glue_sensor)==False:
		time.sleep(0.5)
		GPIO.output(buzzer,True)
		#time.sleep(2)
		print("Glue_sensor detect object")
		#for i in range(3):
		#	pi.write(MODE[i],RESOLUTION['1/8'][i])
		pi.write(STEP,0)
		time.sleep(2)
		pi.set_PWM_dutycycle(STEP,128)
                pi.set_PWM_frequency(STEP,500)
		time.sleep(0.5)
	

except KeyboardInterrupt:
    print ("\nCtrl-C pressed.  Stopping PIGPIO and exiting...")
finally:
    pi.set_PWM_dutycycle(STEP, 0)  # PWM off
    pi.stop()
