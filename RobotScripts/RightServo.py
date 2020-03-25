import RPi.GPIO as GPIO  # Imports the standard Raspberry Pi GPIO library

GPIO.setmode(GPIO.BOARD)  # Sets the pin numbering system to use the physical layout

# Set up pin 12 for PWM
GPIO.setup(12, GPIO.OUT)  # Sets up pin 12 to an output (instead of an input)
pwm = GPIO.PWM(12, 50)  # Sets up pin 11 as a PWM pin | 50hz frequency


def start():
    test = 6.8
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
    change = 6.8 + duty_cycle_number
    # if 6.75 <= change <= 6.85:
    #     pwm.start(0)  # change too small - no need to move (Servo sometimes moves at steady 6.9)
    if change > 7.3:
        pwm.start(7.3)
    elif change < 5.3:
        pwm.start(5.3)
    else:
        pwm.start(change)  # Starts running PWM on the pin and sets it to 1

    # pwm.start(11.5)
    # elif change > 12.5:
    #    pwm.start(12.5)
    # elif change < 0:
    #    pwm.start(0)

    print("Stabilizing using PID: " + str(duty_cycle_number))
    print("DutyCycle using PID: " + str(change))


def stop():
    pwm.stop()  # At the end of the program, stop the PWM
    GPIO.cleanup()  # Resets the GPIO pins back to

# class RightServo:
#
#     def __init__(self):
#         GPIO.setmode(GPIO.BOARD)  # Sets the pin numbering system to use the physical layout
#         GPIO.setup(12, GPIO.OUT)  # Sets up pin 12 (for PWM) to an output (instead of an input)
#         self.pwm = GPIO.PWM(12, 50)  # Sets up pin 12 as a PWM pin
#         self.default_steady_signal = 7.1
#
#     def start(self):
#         self.pwm.start(0)  # Starts running PWM on the pin and sets it
#         # Move the servo back and forth
#         # pwm.ChangeDutyCycle(test)
#
#     def move(self, duty_cycle_number):
#         # Steady signal + the pid value(converted to duty cycles)
#         self.pwm.ChangeDutyCycle(self.default_steady_signal + duty_cycle_number)
#         print("Right motor moved with: " + str(self.default_steady_signal + duty_cycle_number))
#
#     def stop(self):
#         self.pwm.stop()  # At the end of the program, stop the PWM
#         # GPIO.cleanup()  # Resets the GPIO pins back to
