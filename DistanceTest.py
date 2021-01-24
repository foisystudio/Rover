from gpiozero import DistanceSensor
from time import sleep

sensor = DistanceSensor(24, 25)
sensor2 = DistanceSensor(7, 8)

while True:
    print('Distance to nearest object is 1', sensor.distance, 'm')
    sleep(1)
    print('Distance to nearest object is 2 ', sensor2.distance, 'm')
    sleep(1)