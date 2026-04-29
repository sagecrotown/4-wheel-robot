#! /home/sage/Code/.venv/bin/python

from evdev import InputDevice, categorize, ecodes
import evdev
from gpiozero import Device, Motor
from gpiozero.pins.rpigpio import RPiGPIOFactory
import time
import math

Device.pin_factory = RPiGPIOFactory()

# motors are named top to bottom, left to right: 
# 1  2
# 3  4
motor1 = Motor(7, 1)
motor2 = Motor(20, 21)
motor3 = Motor(27, 17)
motor4 = Motor(9, 10)

# devices = [evdev.InputDevice(path) for path in evdev.list_devices()]
# for device in devices:
# 	print(device.path, device.name, device.phys)

dev = evdev.InputDevice('/dev/input/event4')

rot_x = 0
rot_y = 0
x = 0
y = 0
w = 0
vel = 1

print("listening for controller input ... ")

for event in dev.read_loop():
	if event.type == ecodes.EV_ABS:
		print(event.code == ecodes.ABS_RX)

		if event.code == ecodes.ABS_RX or event.code == ecodes.ABS_RY:
			
			if event.code == ecodes.ABS_RX:
				w = -event.value/32767
			
			print("rot: ", w)
			target1 = -w
			target2 = w
			target3 = -w
			target4 = w

		else:
			if event.code == ecodes.ABS_HAT0X or event.code == ecodes.ABS_HAT0Y:

				if event.code == ecodes.ABS_HAT0X:
					y = -event.value
					# print("y: ", y)
				elif event.code == ecodes.ABS_HAT0Y:
					x = -event.value
					# print("x: ", x)

			elif event.code == ecodes.ABS_X or event.code == ecodes.ABS_Y:

				# translate from x to y, the controller has a different sense of direction
				if event.code == ecodes.ABS_X:
					y = -(event.value/32767)
				
				elif event.code == ecodes.ABS_Y:
					x = -(event.value/32767)
					
			# print("input: (", x, ", ", y, ")")

			# add z when I configure rotational inputs from controller	
			target1 = (x + y) / 1.2 
			target2 = (x - y) / 1.2
			target3 = (x - y) / 1.2 
			target4 = (x + y) / 1.2 

		if target1 > 1:
			target1 = 1
		if target2 > 1:
			target2 = 1
		if target3 > 1:
			target3 = 1
		if target4 > 1:
			target4 = 1

		if target1 < -1:
			target1 = -1
		if target2 < -1:
			target2 = -1
		if target3 < -1:
			target3 = -1
		if target4 < -1:
			target4 = -1

		print("targets: (", target1, ", ", target2, ", ", target3, ", ", target4, ")")

		if (target1 > 0):
			motor1.forward(target1)
		elif (target1 < 0): 
			motor1.backward(-target1)
		else:
			motor1.stop()

		if (target2 > 0):
			motor2.forward(target2)
		elif (target2 < 0): 
			motor2.backward(-target2)
		else:
			motor2.stop()

		if (target3 > 0):
			motor3.forward(target3)
		elif (target3 < 0): 
			motor3.backward(-target3)
		else:
			motor3.stop()
            
		if (target4 > 0):
			motor4.forward(target4)
		elif (target4 < 0): 
			motor4.backward(-target4)
		else:
			motor4.stop()