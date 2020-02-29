import RPi.GPIO as GPIO  # Imports the standard Raspberry Pi GPIO library
from time import sleep  # Imports sleep (aka wait or pause) into the program


class LeftServo:

    def __init__(self):
        GPIO.setmode(GPIO.BOARD)  # Sets the pin numbering system to use the physical layout
        GPIO.setup(11, GPIO.OUT)  # Sets up pin 12 (for PWM) to an output (instead of an input)
        self.pwm = GPIO.PWM(11, 50)  # Sets up pin 11 as a PWM pin | 50hz frequency
        self.default_steady_signal = 7.1

    def start(self):
        self.pwm.start(0)  # Starts running PWM on the pin and sets it
        # Move the servo back and forth
        # pwm.ChangeDutyCycle(test)

    def move(self, duty_cycle_number):
        self.pwm.ChangeDutyCycle(self.default_steady_signal + duty_cycle_number)

    def stop(self):
        self.pwm.stop()  # At the end of the program, stop the PWM
        # GPIO.cleanup()  # Resets the GPIO pins back to
