import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)      # disable warnings
GPIO.setmode(GPIO.BCM)      # setup pins based on GPIO #'s
GPIO.setup(27,GPIO.IN)     # button 1 
GPIO.setup(22,GPIO.IN) 	  # button 2
GPIO.setup(17, GPIO.OUT) # servo signal pin

frequency_hertz =50    # servo operating at 50hz
pwm = GPIO.PWM(17, frequency_hertz)

while 1:         
   if (GPIO.input(27) == False):        # turn left
      pwm.start(.1)                    # servo will try 
      time.sleep(.0001)		      # get to the very left position	
      pwm.start(0)  		     # but it turns off everytime we push button
			            # the button pressed will keep turning
				   # left until the very left position
   if (GPIO.input(22) == False):  # turn right
      pwm.start(13)
      time.sleep(.0001)
      pwm.start(0)

