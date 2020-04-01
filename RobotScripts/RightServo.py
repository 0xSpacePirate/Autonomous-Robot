import RPi.GPIO as GPIO  # Imports the standard Raspberry Pi GPIO library
import pigpio
import time

#  GPIO.setmode(GPIO.BOARD)  # Sets the pin numbering system to use the physical layout

# Set up pin 12 for PWM
# GPIO.setup(12, GPIO.OUT)  # Sets up pin 12 to an output (instead of an input)
# pwm = GPIO.PWM(12, 50)  # Sets up pin 11 as a PWM pin | 50hz frequency

frequency = 50
period = 1.0 / frequency
lowestCycle = 0.0005 / period * 100
highestCycle = 0.0025 / period * 100
minAngle = 0
maxAngle = 180
gpioPin = 12  # GPIO pin connected to servo
pi = pigpio.pi()  # connect to GPIO
if not pi.connected:
    print("not connected")
    exit()

pi.set_mode(gpioPin, pigpio.OUTPUT)  # set pin to output mode
print(pi.set_PWM_frequency(gpioPin, frequency))  # set PWM frequency of pin
pi.set_PWM_range(gpioPin, 255)


def start():
    test = 6.8
    # pwm.start(test)  # Starts running PWM on the pin and sets it to 1
    # example = 0.0005 # 500us minimum

    # pwm.ChangeDutyCycle(test)

    pi.set_PWM_range(gpioPin, 255)
    pi.set_servo_pulsewidth(gpioPin, 1000)
    time.sleep(0.5)
    pi.set_servo_pulsewidth(gpioPin, 1450)
    time.sleep(0.5)
    pi.set_servo_pulsewidth(gpioPin, 2000)
    time.sleep(0.5)
    pi.set_servo_pulsewidth(gpioPin, 0)

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


def move(pulse_width_number):
    change = 1450 + pulse_width_number
    # if 6.75 <= change <= 6.85:
    #     pwm.start(0)  # change too small - no need to move (Servo sometimes moves at steady 6.9)

    # if change > 7.3:
    #     pwm.start(7.3)
    # elif change < 5.3:
    #     pwm.start(5.3)
    # else:
    #     pwm.start(change)  # Starts running PWM on the pin and sets it to 1
    print("PULSE WIDTH: " + str(change))

    if change > 2000:
        pi.set_servo_pulsewidth(gpioPin, 2000)
    elif change < 1000:
        pi.set_servo_pulsewidth(gpioPin, 1000)
    else:
        pi.set_servo_pulsewidth(gpioPin, change)

    # print("Stabilizing using PID: " + str(duty_cycle_number))
    # print("DutyCycle using PID: " + str(change))


def stop():
    # pwm.stop()  # At the end of the program, stop the PWM
    GPIO.cleanup()  # Resets the GPIO pins back to
    pi.stop()
