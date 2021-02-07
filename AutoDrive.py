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
FrontDistance = [0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0]
RearDistance = [0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0] 


def Front_Sornar():
    f_sonar_servo.value = -1
    sleep(0.2)
    FrontDistance[0] = front_sensor.distance
    print('0 deg = ', front_sensor.distance)
    f_sonar_servo.value = -0.75
    sleep(0.2)
    FrontDistance[1] = front_sensor.distance
    print('22.5 deg = ', front_sensor.distance)
    f_sonar_servo.value = -0.5
    sleep(0.2)
    FrontDistance[2] = front_sensor.distance
    print('45 deg = ', front_sensor.distance)
    f_sonar_servo.value = -0.25
    sleep(0.2)
    FrontDistance[3] = front_sensor.distance
    print('67.5 deg = ', front_sensor.distance)
    f_sonar_servo.value = 0
    sleep(0.2)
    FrontDistance[4] = front_sensor.distance
    print('90 deg = ', front_sensor.distance)
    f_sonar_servo.value = 0.25
    sleep(0.2)
    FrontDistance[5] = front_sensor.distance
    print('112.5 deg = ', front_sensor.distance)
    f_sonar_servo.value = 0.5
    sleep(0.2)
    FrontDistance[6] = front_sensor.distance
    print('135 deg = ', front_sensor.distance)
    f_sonar_servo.value = 0.75
    sleep(0.2)
    FrontDistance[7] = front_sensor.distance
    print('157.5 deg = ', front_sensor.distance)
    f_sonar_servo.value = 1
    sleep(0.2)
    FrontDistance[8] = front_sensor.distance
    print('180 deg = ', front_sensor.distance)

def Rear_Sonar():
    back_servo.value = -1
    sleep(0.2)
    RearDistance[0] = back_sensor.distance
    back_servo.value = -0.75
    sleep(0.2)
    RearDistance[0] = back_sensor.distance
    back_servo.value = -0.5
    sleep(0.2)
    RearDistance[0] = back_sensor.distance
    back_servo.value = -0.25
    sleep(0.2)
    RearDistance[0] = back_sensor.distance
    back_servo.value = 0
    sleep(0.2)
    RearDistance[0] = back_sensor.distance
    back_servo.value = 0.25
    sleep(0.2)
    RearDistance[0] = back_sensor.distance
    back_servo.value = 0.5
    sleep(0.2)
    RearDistance[0] = back_sensor.distance
    back_servo.value = 0.75
    sleep(0.2)
    RearDistance[0] = back_sensor.distance
    back_servo.value = 1
    sleep(0.2)
    RearDistance[0] = back_sensor.distance

def Look():
    f_cam_servo.mid()
    f_cam_servo.min()
    sleep(1)
    f_cam_servo.mid()
    sleep(1)
    f_cam_servo.max()
    sleep(1)
    f_cam_servo.mid()

    
### NEED WORK ### 
### Kinda works but not well :( ###
def Check_direction():
    if FrontDistance[3] > 0.25 and FrontDistance[4] > 0.25 and FrontDistance[5] > 0.25:
        print('67.5 deg is > 0.25m and 90 deg > 0.25m and 112.5 deg > 0.25m')
        print('so go forward') 
        robot.forward()
        sleep(0.5)
        robot.stop()
    elif FrontDistance[3] < 0.25 or FrontDistance[4] < 0.25 or FrontDistance[5] < 0.25:
        print('67.5 deg is < 0.25m and 90 deg < 0.25m and 112.5 deg < 0.25m')
        print('Check which way to go') 
        if (FrontDistance[0] and FrontDistance[1]) > (FrontDistance[7] and FrontDistance[8]):
            print('0 deg and 22.5 deg > 157.5 deg and 180 deg')
            print('turn left')
            robot.left()
            sleep(0.5)
            robot.stop()
        if  (FrontDistance[0] and FrontDistance[1]) < (FrontDistance[7] and FrontDistance[8]):
            print('0 deg and 22.5 deg < 157.5 deg and 180 deg')
            print('go right')
            robot.right()
            sleep(0.5)
            robot.stop()
    else:
        print('no critera met go backwards')
        robot.backward()
        sleep(0.5)
        robot.stop()
    
while True:    
    Front_Sornar()
    Rear_Sonar()
    Check_direction()

