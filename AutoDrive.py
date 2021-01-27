#Import libs
from gpiozero import Robot
from gpiozero import DistanceSensor
from gpiozero import Servo
from time import sleep
from signal import pause
from gpiozero.pins.pigpio import PiGPIOFactory

#Calibrate Servos
myCorrection=0.5
maxPW=(2.0+myCorrection)/1000
minPW=(1.0-myCorrection)/1000

#Set Servo Pins
myGPIO1=15 #back servo
myGPIO2=18 #front sonar servo
myGPIO3=23 #front camera servo
#Create Servos
back_servo = Servo(myGPIO1,min_pulse_width=minPW,max_pulse_width=maxPW,pin_factory = PiGPIOFactory())
f_sonar_servo = Servo(myGPIO2,min_pulse_width=minPW,max_pulse_width=maxPW,pin_factory = PiGPIOFactory())
f_cam_servo = Servo(myGPIO3,min_pulse_width=minPW,max_pulse_width=maxPW,pin_factory = PiGPIOFactory())

#Create Robot motors
robot = Robot(left=(12, 16), right=(21, 20))

#Create Sonar devices
front_sensor = DistanceSensor(7, 8)
back_sensor = DistanceSensor(24, 25)

#Intilize Vars
FrontForward = 0.0
FrontRigth = 0.0
FrontLeft = 0.0
RearForward = 0.0
RearLeft = 0.0
RearRight = 0.0

