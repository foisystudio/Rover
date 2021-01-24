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


 
while True:
    servo1.mid()
    print("1 mid")
    sleep(0.2)
    servo1.min()
    print("1 min")
    sleep(0.2)
    servo1.mid()
    print("1 mid")
    sleep(0.2)
    servo1.max()
    print("1 max")
    sleep(0.2)

    servo2.mid()
    print("2 mid")
    sleep(0.2)
    servo2.min()
    print("2 min")
    sleep(0.2)
    servo2.mid()
    print("2 mid")
    sleep(0.2)
    servo2.max()
    print("2 max")
    sleep(0.2)

    servo3.mid()
    print("3 mid")
    sleep(0.2)
    servo3.min()
    print("3 min")
    sleep(0.2)
    servo3.mid()
    print("3 mid")
    sleep(0.2)
    servo3.max()
    print("3 max")
    sleep(0.2)
