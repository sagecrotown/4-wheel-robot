#! /home/sage/Code/.venv/bin/python

from evdev import InputDevice, categorize, ecodes
import evdev
from gpiozero import Device, Motor
from gpiozero.pins.rpigpio import RPiGPIOFactory
import time

Device.pin_factory = RPiGPIOFactory()

# named top to bottom, left to right: 
# 1  2
# 3  4
motor1 = Motor(forward=7, backward=1)
motor2 = Motor(forward=20, backward=21)
motor3 = Motor(forward=27,backward=17)
motor4 = Motor(forward=9,backward=10)

# motor1.forward()
# time.sleep(1)
# motor1.stop()
# motor2.forward()
# time.sleep(1)
# motor2.stop()
# motor3.forward()
# time.sleep(1)
# motor3.stop()
# motor4.forward()
# time.sleep(1)
# motor4.stop()

devices = [evdev.InputDevice(path) for path in evdev.list_devices()]
for device in devices:
	print(device.path, device.name, device.phys)

dev = evdev.InputDevice('/dev/input/event4')

hat_x = 0
hat_y = 0
x = 0
y = 0
vel = 1

def left(vel):
	motor1.backward(speed=vel)
	motor2.forward(speed=vel)
	motor3.backward(speed=vel)
	motor4.forward(speed=vel)


def right(vel):
	motor1.forward(speed=vel)
	motor2.backward(speed=vel)
	motor3.forward(speed=vel)
	motor4.backward(speed=vel)

def forward(vel):
	motor1.forward(speed=vel)
	motor2.forward(speed=vel)
	motor3.forward(speed=vel)
	motor4.forward(speed=vel)

def backward(vel):
	motor1.backward(speed=vel)
	motor2.backward(speed=vel)
	motor3.backward(speed=vel)
	motor4.backward(speed=vel)

def stop():
	motor1.stop()
	motor2.stop()
	motor3.stop()
	motor4.stop()


print("listening for controller input ... ")

for event in dev.read_loop():
	if event.type == ecodes.EV_ABS:

		if event.code == ecodes.ABS_HAT0X or event.code == ecodes.ABS_HAT0Y:

			if event.code == ecodes.ABS_HAT0X:
				hat_x = event.value
				print("x: ", hat_x)
			elif event.code == ecodes.ABS_HAT0Y:
				hat_y = event.value
				print("y: ", hat_y)

			if hat_y == -1:
				forward(vel)
			elif hat_y == 1:
				backward(vel)
			elif hat_x == -1:
				left(vel)
			elif hat_x == 1:
				right(vel)
			elif hat_x == 0 and hat_y == 0:
				stop()

		elif event.code == ecodes.ABS_X or event.code == ecodes.ABS_Y:

			if event.code == ecodes.ABS_X:
				x = (event.value/32767)
				print("x: ", x)
			elif event.code == ecodes.ABS_Y:
				y = (event.value/32767)
				print("y: ", y)


# TODO:
# write functions to combine robot targets into motor signals
# left joystick should control movement (foward, backward, strafe left, strafe right)
# right joystick should control pose
# will need mecanum equations for this bit
# will need to rewrite drive equations
			

			if y < 0:
				# print("forward")
				# forward(abs(y))
				pass
			elif y > 0:
				# print("backward")
				# backward(y)
				pass
			
			if x < 0:
				left(abs(x))
			elif x > 0:
				right(x)
			elif x == 0 and y == 0:
				stop()
