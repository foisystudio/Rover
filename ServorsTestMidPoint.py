from gpiozero import Servo
from time import sleep
from gpiozero.pins.pigpio import PiGPIOFactory
 
myGPIO1=23 #back
myGPIO2=18 #front sonar
myGPIO3=15 #front camera
 
myCorrection=0.5
maxPW=(2.0+myCorrection)/1000
minPW=(1.0-myCorrection)/1000
 
servo1 = Servo(myGPIO1,min_pulse_width=minPW,max_pulse_width=maxPW,pin_factory = PiGPIOFactory())
servo2 = Servo(myGPIO2,min_pulse_width=minPW,max_pulse_width=maxPW,pin_factory = PiGPIOFactory())
servo3 = Servo(myGPIO3,min_pulse_width=minPW,max_pulse_width=maxPW,pin_factory = PiGPIOFactory())

servo1.mid()
servo2.mid()
servo3.mid()