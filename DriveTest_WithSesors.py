from gpiozero import Robot
from gpiozero import DistanceSensor
from gpiozero import Servo
from time import sleep
from signal import pause
from gpiozero.pins.pigpio import PiGPIOFactory

myCorrection=0.5
maxPW=(2.0+myCorrection)/1000
minPW=(1.0-myCorrection)/1000


myGPIO1=15 #back servo
myGPIO2=18 #front sonar servo
myGPIO3=23 #front camera servo

back_servo = Servo(myGPIO1,min_pulse_width=minPW,max_pulse_width=maxPW,pin_factory = PiGPIOFactory())
f_sonar_servo = Servo(myGPIO2,min_pulse_width=minPW,max_pulse_width=maxPW,pin_factory = PiGPIOFactory())
f_cam_servo = Servo(myGPIO3,min_pulse_width=minPW,max_pulse_width=maxPW,pin_factory = PiGPIOFactory())

robot = Robot(left=(12, 16), right=(21, 20))

front_sensor = DistanceSensor(7, 8)
back_sensor = DistanceSensor(24, 25)

#set all servors to mid point
back_servo.mid() 
f_sonar_servo.mid()
f_cam_servo.mid()
#set inital distances
distance_front = 0.02
distance_back = 0.02
distance_front = front_sensor.distance
distance_back = back_sensor.distance


while True:


    

    #Check Barrings front
    f_sonar_servo.mid()
    print("front forward")
    sleep(0.5)
    print('Distance to nearest object is', front_sensor.distance, 'm')
    f_sonar_servo.min()
    print("front right")
    sleep(0.5)
    print('Distance to nearest object is', front_sensor.distance, 'm')
    f_sonar_servo.mid()
    print("front forward")
    sleep(0.5)
    print('Distance to nearest object is', front_sensor.distance, 'm')
    f_sonar_servo.max()
    print("front left")
    sleep(0.5)
    print('Distance to nearest object is', front_sensor.distance, 'm')
    f_sonar_servo.mid()
    distance_front = front_sensor.distance
    
    #Check Barrings back
    back_servo.mid()
    print("back forward")
    sleep(0.5)
    print('Distance to nearest object is', back_sensor.distance, 'm')
    back_servo.min()
    print("back right")
    sleep(0.5)
    print('Distance to nearest object is', back_sensor.distance, 'm')
    back_servo.mid()
    print("back forward")
    sleep(0.5)
    print('Distance to nearest object is', back_sensor.distance, 'm')
    back_servo.max()
    print("back left")
    sleep(0.5)
    print('Distance to nearest object is', back_sensor.distance, 'm')
    back_servo.mid()
    distance_back = back_sensor.distance

    #ask
    userInput = input("which direction (F/B/R/L/look):\n")
    #if user enters exit exit program
    if userInput == "exit":
        break
        robot.stop()
    #Go Direction of user input
    if userInput == "F":
        robot.forward()
        sleep(1)
        robot.stop()
    if userInput == "B":
        robot.backward()
        sleep(1)
        robot.stop()
    if userInput == "R":
        robot.right()
        sleep(0.5)
        robot.stop()
    if userInput == "L":
        robot.left()
        sleep(0.5)
        robot.stop()
    if userInput == "f":
        robot.forward()
        sleep(0.2)
        robot.stop()
    if userInput == "b":
        robot.backward()
        sleep(0.2)
        robot.stop()
    if userInput == "r":
        robot.right()
        sleep(0.2)
        robot.stop()
    if userInput == "l":
        robot.left()
        sleep(0.2)
        robot.stop()
    #if user wants to look
    if userInput == "look":
        userInput2 = input("which direction (F/R/L:\n")
        if userInput2 == "F":
            f_cam_servo.mid()
        if userInput2 == "R":
            f_cam_servo.min()
            sleep(1)
            f_cam_servo.mid()
        if userInput2 == "L":
            f_cam_servo.max()
            sleep(1)
            f_cam_servo.mid()

            
            