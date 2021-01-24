from gpiozero import Robot
from time import sleep
from signal import pause

robot = Robot(left=(20, 21), right=(12, 16))

for i in range(4):
    robot.forward()
    sleep(1)
    robot.right()
    sleep(1)
    robot.left()
    sleep(1)
robot.stop()

for i in range(4):
    robot.backward()
    sleep(1)
    robot.left()
    sleep(1)

robot.stop()
