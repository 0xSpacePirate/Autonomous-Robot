import RPi.GPIO as GPIO
import time
from LeftServo import LeftServo
# from RightServo import RightServo
import RightServo as rightMotor
from threading import Thread
# import GyroReader as gyroScope
from GyroFilter import GyroFilter
from PIDBalancer import PIDBalancer
from PIDController import PIDController
from threading import Timer


class Robot:
    print("Launch Configuration initiated")

    # DutyCycle = 1/18 * (DesiredAngle) + 2 (or + 2.5 -> check)

    def __init__(self):
        self.pid_balancer = PIDBalancer(1.0, 1.0, 1.0)
        self.gyroFilter = self.pid_balancer.get_gyro_filter()
        (self.gyro_scaled_x, self.gyro_scaled_y, self.gyro_scaled_z,
         self.accel_scaled_x, self.accel_scaled_y, self.accel_scaled_z) = self.gyroFilter.get_gyro_and_accel()
        # self.rightMotor = RightServo()
        self.leftMotor = LeftServo()

    def start_motors(self):
        # leftMotor.start()
        # self.rightMotor.start()
        rightMotor.start()
        print("Motors started")

    def stop_motors(self):
        # leftMotor.stop()
        # self.rightMotor.stop()
        rightMotor.stop()
        GPIO.cleanup()
        print("Motors stopped")

    def move_left(self):
        self.start_motors()
        left = 7.5  # move towards 90 degrees
        # self.rightMotor.stop()
        rightMotor.stop()
        self.leftMotor.move(left)

    def move_right(self):
        self.start_motors()
        right = 7.5  # move towards 90 degrees
        self.leftMotor.stop()
        # rightMotor.move(right)
        # self.rightMotor.move(right)
        rightMotor.move(right)

    def move_forward(self):
        self.start_motors()
        # forward = 5.5  # pid_value  # emphasizes that the pid value is being used
        # self.leftMotor.move(forward)
        # self.rightMotor.move(forward)

    def move_backwards(self):
        self.start_motors()
        # backwards = 12  # pid_value  # emphasizes that the pid value is being used
        # self.leftMotor.move(backwards)
        # self.rightMotor.move(backwards)

    def move_back(self):
        self.start_motors()
        back = 12.5
        # self.rightMotor.stop()
        rightMotor.stop()
        self.leftMotor.move(back)

    def set_angle(self, angle):
        duty = (1 / 36) * angle + 2
        return duty

    def balance(self):
        # gyroScope.print_all_data()
        print("\n\n------------ PID + Filter Below ---------------\n\n")
        # gyroFilter.print_all()
        # self.start_motors()

        try:
            while True:
                self.gyroFilter.print_all()
                self.pid_balancer.update_pid_error()
                pid_value = self.pid_balancer.get_pid_value()
                print("PID value = " + str(pid_value()))
                # threading.Timer(0.5, self.stabilize(pid_value)).start() # TODO not thread safe
                self.stabilize(pid_value())
                # self.move_forward()
                self.gyroFilter.print_all()
                time.sleep(0.1)
                # self.stop_motors()
        except KeyboardInterrupt:
            print("Interrupted. End of stabilizing")

        # self.gyroFilter.print_all()
        # pid_value = self.pid_balancer.get_pid_value()
        # self.pid_balancer.update_pid_error()
        # # self.move_forward()
        # self.stabilize(pid_value())
        # self.gyroFilter.print_all()
        # (x, y) = self.gyroFilter.calc_xy_values()
        # print("X and Y ->  " + str(x) + " : " + str(y))

    def stabilize(self, pid_value):
        # DutyCycle = PulseWidth/Period, therefore
        # DutyCycle = PulseWidth/(1/frequency) = PulseWidth * frequency
        # DutyCycle = PulseWidth*frequency = .001*50=.05= 5%
        print("pid_value is: " + str(pid_value))
        pid = pid_value / 100  # Interpolate the number so it's compatible with the PWM signal
        # self.rightMotor.move(pid)
        rightMotor.move(pid)
        # if pid_value > 0:
        #     self.move_forward()
        # else:
        #     self.move_backwards()
        # self.stop_motors()

# stop_motors()
