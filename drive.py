#! /home/sage/Code/.venv/bin/python

from gpiozero import Motor
from gpiozero import Device
from gpiozero.pins.rpigpio import RPiGPIOFactory
import time

Device.pin_factory = RPiGPIOFactory()

motor1 = Motor(forward = 7, backward = 1)
motor2 = Motor(forward = 20, backward = 21)
motor3 = Motor(forward = 27, backward = 17)
motor4 = Motor(forward = 9, backward = 10)

#motor1.forward()
#time.sleep(1)
#motor1.forward(speed = 0.5)
#time.sleep(1)
#motor1.stop()

#motor2.forward()
#time.sleep(1)
#motor2.forward(speed = 0.5)
#time.sleep(1)
#motor2.stop()

#motor3.forward()
#time.sleep(1)
#motor3.forward(speed = 0.5)
#time.sleep(1)
#motor3.stop()

#motor4.forward()
#time.sleep(1)
#motor4.forward(speed = 0.5)
#time.sleep(1)
#motor4.stop()

motor1.forward()
motor2.forward()
motor3.forward()
motor4.forward()
time.sleep(4)
motor1.stop()
motor2.stop()
motor3.stop()
motor4.stop()
