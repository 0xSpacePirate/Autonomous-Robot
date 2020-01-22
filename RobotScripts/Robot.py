import RPi.GPIO as GPIO
import time
import LeftServo as leftMotor
import RightServo as rightMotor
from threading import Thread

print("Launch Configuration initiated")



def startMotors():
	leftMotor.start()
	rightMotor.start()
	print("Motors started")


def stopMotors():
	leftMotor.stop()
	rightMotor.stop()
	GPIO.cleanup()
	print("Motors stopped")


def turnLeft():
	left = 7.5 # turn towards 90 degrees
	rightMotor.stop()
	leftMotor.turn(left)


def turnRight():
	right = 7.5  # turn towards 90 degrees
	leftMotor.stop()
	rightMotor.turn(right)


def turnBack():	
	back = 12.5 # turn backwards 180 degrees
	rightMotor.stop()
	leftMotor.turn(12.5)


startMotors()

turnLeft()
turnRight()
turnBack()

stopMotors()










