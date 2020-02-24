import RPi.GPIO as GPIO  # Imports the standard Raspberry Pi GPIO library
from time import sleep  # Imports sleep (aka wait or pause) into the program

GPIO.setmode(GPIO.BOARD)  # Sets the pin numbering system to use the physical layout

# Set up pin 12 for PWM
GPIO.setup(12, GPIO.OUT)  # Sets up pin 12 to an output (instead of an input)
pwm = GPIO.PWM(12, 50)  # Sets up pin 11 as a PWM pin | 50hz frequency


def start():
    test = 7.6
    pwm.start(test)  # Starts running PWM on the pin and sets it to 1
    # example = 0.0005 # 500us minimum

    pwm.ChangeDutyCycle(test)

    # Generally a 10 us change in
    # pulse width results in a 1 degree change in angle

    # Move the servo back and forth
    # dutyCycle = 1.0
    # print("Duty cycle: " + str(dutyCycle))
    # pwm.ChangeDutyCycle(10)
    # sleep(3)
    # p.ChangeDutyCycle(2.5)
    # sleep(3)
    # p.ChangeDutyCycle(0.5)  # Changes the pulse width to 3 (so moves the servo)
    # sleep(3)  # Wait 1 second
    # p.ChangeDutyCycle(2.5)  # Changes the pulse width to 12 (so moves the servo)
    # sleep(3)
    # p.ChangeDutyCycle(3.5)
    # sleep(3)
    # p.ChangeDutyCycle(0.5)


def move(duty_cycle_number):
    pwm.ChangeDutyCycle(duty_cycle_number)


def stop():
    pwm.stop()  # At the end of the program, stop the PWM
    # GPIO.cleanup()  # Resets the GPIO pins back to

# start()
# stop()
