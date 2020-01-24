import RPi.GPIO as GPIO
import time
import LeftServo as leftMotor
import RightServo as rightMotor
from threading import Thread
#import GyroReader as gyroScope
import GyroFilter as gyroFilter
import PIDBalancer as pidBalancer

print("Launch Configuration initiated")


def start_motors():
	leftMotor.start()
	rightMotor.start()
	print("Motors started")


def stop_motors():
	leftMotor.stop()
	rightMotor.stop()
	GPIO.cleanup()
	print("Motors stopped")


def move_left():
	start_motors()
	left = 7.5  # move towards 90 degrees
	rightMotor.stop()
	leftMotor.move(left)


def move_right():
	start_motors()
	right = 7.5  # move towards 90 degrees
	leftMotor.stop()
	rightMotor.move(right)


def move_forward(pid_value):
	start_motors()
	forward = pid_value  # emphasizes that the pid value is being used
	leftMotor.move(forward)
	rightMotor.move(forward)


def move_backwards(pid_value):
	start_motors()
	backwards = pid_value  # emphasizes that the pid value is being used
	leftMotor.move(backwards)
	rightMotor.move(backwards)


def move_back():
	start_motors()
	back = 12.5  # move backwards 180 degrees
	rightMotor.stop()
	leftMotor.move(back)


def balance():
	#gyroScope.print_all_data()
	print("\n\n------------ PID + Filter Below ---------------\n\n")
	gyroFilter.print_all()
	start_motors()

	try:
		for i in range(0, 100000):
			gyroFilter.print_all()
			leftMotor.stop()
			rightMotor.stop()
			time.sleep(2)
			stabilize()
			gyroFilter.print_all()
	except KeyboardInterrupt:
		print("Interrupted. End of stabilizing")

	# move_left()
	# move_right()
	# move_back()


def stabilize():
	start_motors()
	pid_value = pidBalancer.get_pid_value()
	if pidBalancer.get_pid_value() > 0:
		move_forward(pid_value)
	else:
		move_backwards(pid_value)


balance()

stop_motors()










