import RPi.GPIO as GPIO  # Imports the standard Raspberry Pi GPIO library
from time import sleep  # Imports sleep (aka wait or pause) into the program

GPIO.setmode(GPIO.BOARD)  # Sets the pin numbering system to use the physical layout

# Set up pin 11 for PWM
GPIO.setup(11, GPIO.OUT)  # Sets up pin 11 to an output (instead of an input)
p = GPIO.PWM(11, 50)  # Sets up pin 11 as a PWM pin | 50hz frequency


def start():
    p.start(0)  # Starts running PWM on the pin and sets it to 0
    # Move the servo back and forth
    # p.ChangeDutyCycle(0)  # Changes the pulse width to 3 (so moves the servo)
    # sleep(2)
    # p.ChangeDutyCycle(2) # sleep(2)  # Wait 1 second
    # p.ChangeDutyCycle(0)  # Changes the pulse width to 12 (so moves the servo)
    # sleep(2)
    # p.ChangeDutyCycle(12)
    # sleep(2)
    # p.ChangeDutyCycle(4.5)


def move(duty_cycle_number):
    print("Left servo: " + duty_cycle_number)
    # p.ChangeDutyCycle(1)
    # sleep()


def stop():
    p.stop()  # At the end of the program, stop the PWM
    # GPIO.cleanup()  # Resets the GPIO pins back to defaults

# start()
# stop()
