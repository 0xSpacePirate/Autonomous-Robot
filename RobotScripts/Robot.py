import RPi.GPIO as GPIO
import time
import LeftServo as leftMotor
import RightServo as rightMotor
from threading import Thread
# import GyroReader as gyroScope
import GyroFilter as gyroFilter
from PIDBalancer import PIDBalancer
from PIDController import PIDController


class Robot:
    print("Launch Configuration initiated")



    # DutyCycle = 1/18 * (DesiredAngle) + 2 (or + 2.5 -> check)

    def __init__(self):
        self.pid_balancer = PIDBalancer(1.0, 1.0, 1.0)
        (self.gyro_scaled_x, self.gyro_scaled_y, self.gyro_scaled_z,
        self.accel_scaled_x, self.accel_scaled_y, self.accel_scaled_z) = gyroFilter.read_all()

    def start_motors(self):
        # leftMotor.start()
        rightMotor.start()
        print("Motors started")

    def stop_motors(self):
        # leftMotor.stop()
        rightMotor.stop()
        GPIO.cleanup()
        print("Motors stopped")

    def move_left(self):
        self.start_motors()
        left = 7.5  # move towards 90 degrees
        rightMotor.stop()
        leftMotor.move(left)

    def move_right(self):
        self.start_motors()
        right = 7.5  # move towards 90 degrees
        leftMotor.stop()
        rightMotor.move(right)

    def move_forward(self):
        self.start_motors()
        # forward = 5.5  # pid_value  # emphasizes that the pid value is being used
        # leftMotor.move(forward)
        # rightMotor.move(forward)

    def move_backwards(self):
        self.start_motors()
        # backwards = 12  # pid_value  # emphasizes that the pid value is being used
        #   leftMotor.move(backwards)
        # rightMotor.move(backwards)

    def move_back(self):
        self.start_motors()
        back = 12.5  # move backwards 180 degrees
        rightMotor.stop()
        leftMotor.move(back)

    def set_angle(self, angle):
        duty = (1 / 36) * angle + 2
        return duty

    def balance(self):
        # gyroScope.print_all_data()
        print("\n\n------------ PID + Filter Below ---------------\n\n")
        # gyroFilter.print_all()
        # start_motors()

        try:
            while True:
                gyroFilter.print_all()
                pid_value = self.pid_balancer.get_pid_value()
                print("PID value = " + str(pid_value))
                self.stabilize()
                # self.move_forward()
                gyroFilter.print_all()
                # self.stop_motors()
        except KeyboardInterrupt:
            print("Interrupted. End of stabilizing")

    # move_left()
    # move_right()
    # move_back()

    def stabilize(self):
        # DutyCycle = PulseWidth/Period, therefore
        # DutyCycle = PulseWidth/(1/frequency) = PulseWidth * frequency
        # DutyCycle = PulseWidth*frequency = .001*50=.05= 5%
        pid_value = self.pid_balancer.get_pid_value()
        if self.gyro_scaled_y > 5.50:
            self.move_forward()
        elif self.gyro_scaled_y < 5.50:
            self.move_backwards()
        else:
            print("At 5.50 NOW")
        # if pid_value > 0:
        #     self.move_forward()
        # else:
        #     self.move_backwards()
        # self.stop_motors()

# stop_motors()
