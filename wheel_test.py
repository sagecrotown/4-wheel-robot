#! /home/sage/Code/.venv/bin/python

import RPi.GPIO as gpio
import time

def init():
	gpio.setmode(gpio.BCM)

	gpio.setup(17, gpio.OUT)	# back left
	gpio.setup(27, gpio.OUT)	# back left
	gpio.setup(10, gpio.OUT)	# back right
	gpio.setup(9, gpio.OUT)		# back right

	gpio.setup(7, gpio.OUT)		# front left
	gpio.setup(1, gpio.OUT)		# front left
	gpio.setup(20, gpio.OUT)	# front right
	gpio.setup(21, gpio.OUT)	# front right

def forward1(sec):	# back left forward
	gpio.output(17, False)
	gpio.output(27, True)
	print("motor 1 went")

def forward2(sec):	# back right forward
	gpio.output(10, False)
	gpio.output(9, True)
	print("motor 2 went")

def stop2():
	gpio.output(10, False)
	gpio.output(9, False)
	print("motor 2 stopped")

init()
print("back left forward")
forward1(3)
#stop2()
time.sleep(1.5)
#print("back right forward")
#forward2(3)
#time.sleep(1.5)
gpio.cleanup()
