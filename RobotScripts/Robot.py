import RPi.GPIO as GPIO
import time
import LeftServo as leftMotor
import RightServo as rightMotor
from threading import Thread
# import GyroReader as gyroScope
import GyroFilter as gyroFilter
import PIDBalancer as pidBalancer

print("Launch Configuration initiated")


# DutyCycle = 1/18 * (DesiredAngle) + 2 (or + 2.5 -> check)


def start_motors():
    # leftMotor.start()
    rightMotor.start()
    print("Motors started")


def stop_motors():
    # leftMotor.stop()
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
    # forward = 5.5  # pid_value  # emphasizes that the pid value is being used
    # leftMotor.move(forward)
    # rightMotor.move(forward)


def move_backwards(pid_value):
    start_motors()
    # backwards = 12  # pid_value  # emphasizes that the pid value is being used
    # leftMotor.move(backwards)
    # rightMotor.move(backwards)


def move_back():
    start_motors()
    back = 12.5  # move backwards 180 degrees
    rightMotor.stop()
    leftMotor.move(back)


def set_angle(angle):
    duty = (1 / 36) * angle + 2
    return duty


def balance():
    # gyroScope.print_all_data()
    print("\n\n------------ PID + Filter Below ---------------\n\n")
    # gyroFilter.print_all()
    # start_motors()

    try:
        # while True:
        gyroFilter.print_all()
        pid_value = pidBalancer.get_pid_value()
        # leftMotor.stop()
        # move_backwards(0)
        gyroFilter.print_all()
        # time.sleep(0.1)
        gyroFilter.print_all()
        move_forward(0)
        gyroFilter.print_all()
        # rightMotor.stop()
        # time.sleep(0.1)
        # stabilize()
        gyroFilter.print_all()
        stop_motors()
    except KeyboardInterrupt:
        print("Interrupted. End of stabilizing")


# move_left()
# move_right()
# move_back()


def stabilize():
    # DutyCycle = PulseWidth/Period, therefore
    # DutyCycle = PulseWidth/(1/frequency) = PulseWidth * frequency
    # DutyCycle = PulseWidth*frequency = .001*50=.05= 5%
    start_motors()
    pid_value = pidBalancer.get_pid_value()
    if pidBalancer.get_pid_value() > 0:
        move_forward(pid_value)
    else:
        move_backwards(pid_value)
    stop_motors()


balance()

# stop_motors()
