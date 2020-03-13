import smbus
import math
import time
# import simple_pid
from GyroFilter import GyroFilter
from PIDController import PIDController


# For more information refer to tests/balance_numbers_tests.txt
# Gyroscope Average Values;
# Vertical: x = 5.7, y = 7.052; Steady
# Left: x = 6.09, y = 5.946
# Right: x = 5.378, y = 5.946
# ====================
# Accelerometer Average Values
# Vertical: x = -0.173, y = 0.05, z = 1.07; Steady
# Left: x = -0.64, y = 0.122, z = 0.829
# Right: x = 0.66, y = 0.04, z = 0.848

class PIDBalancer:

    def __init__(self, kp, ki, kd):
        self.kp = kp
        self.ki = ki
        self.kd = kd

        self.gyro_vertical_center_x = 5.7
        self.gyro_vertical_center_y = 7.052

        self.median_filter = [0.0, 0.0, 0.0, 0.0, 0.0]
        gyro_scale = 131.0
        accel_scale = 16384.0
        RAD_TO_DEG = 57.29578
        M_PI = 3.14159265358979323846
        now = time.time()
        K = 0.98
        K1 = 1 - K

        time_diff = 0.01
        gyroAngleX = 0.0
        gyroAngleY = 0.0
        gyroAngleZ = 0.0
        accAngX = 0.0
        CFangleX = 0.0
        CFangleX1 = 0.0
        K = 0.98
        FIX = -12.89

        self.gyroFilter = GyroFilter()
        (self.gyro_scaled_x, self.gyro_scaled_y, self.gyro_scaled_z, self.accel_scaled_x, self.accel_scaled_y,
         self.accel_scaled_z) = self.gyroFilter.read_all()
        (self.accel_vertical_center_x, self.accel_vertical_center_y,
         self.accel_vertical_center_z) = self.gyroFilter.get_accel_center_xyz()
        pid_set_point = 0.00
        self.pid = PIDController(kp, ki, kd, pid_set_point)

        # The angle of the Gyroscope
        gyroAngleX += self.gyro_scaled_x * time_diff
        gyroAngleY += self.gyro_scaled_y * time_diff
        gyroAngleZ += self.gyro_scaled_z * time_diff

        accAngX = (math.atan2(self.accel_scaled_x, self.accel_scaled_y) + M_PI) * RAD_TO_DEG
        # math.atan2 numeric value between -PI and PI representing the angle theta of an (x, y) point.
        CFangleX = K * (CFangleX + self.gyro_scaled_x * time_diff) + (1 - K) * accAngX

        accAngX1 = self.get_x_rotation(self.accel_scaled_x, self.accel_scaled_y, self.gyro_scaled_z)
        # accAngX1 = get_x_rotation(accel_scaled_x, accel_scaled_y, gyro_scaled_x) or this one - test?

        CFangleX1 = (K * (CFangleX1 + self.gyro_scaled_x * time_diff) + (1 - K) * accAngX1)

    def dist(self, a, b):
        return math.sqrt((a * a) + (b * b))

    def get_y_rotation(self, x, y, z):
        radians = math.atan2(x, self.dist(y, z))
        return -math.degrees(radians)

    def get_x_rotation(self, x, y, z):
        radians = math.atan2(y, self.dist(x, z))
        return math.degrees(radians)

    def update_pid_error(self):
        average_accel_scaled_x = self.output_filter()
        pid_error = self.accel_vertical_center_x + average_accel_scaled_x  # TODO USE accel_y && accel_z as well?
        print("center: " + str(self.accel_vertical_center_x) + " current(AVG): " + str(average_accel_scaled_x) + " = " + str(pid_error))
        self.pid.update_pid(pid_error)

    def get_pid_value(self):
        print("Current XYZ: " + str(self.accel_scaled_x) + " | " + str(self.accel_scaled_y) + " | " + str(self.accel_scaled_z))
        return self.pid.get_pid

    def get_gyro_filter(self):
        return self.gyroFilter

    def output_filter(self):
        (self.gyro_scaled_x, self.gyro_scaled_y, self.gyro_scaled_z, self.accel_scaled_x, self.accel_scaled_y,
        self.accel_scaled_z) = self.gyroFilter.read_all()
        self.median_filter.insert(0, self.accel_scaled_x)
        self.median_filter.pop()
        average_accel_scaled_x = sum(self.median_filter) / len(self.median_filter)
        return average_accel_scaled_x

    # print(
    #    "{0:.2f} {1:.2f} {2:.2f} {3:.2f} | {4:.2f} {5:.2f} | {}".format(gyroAngleX, gyroAngleY, accAngX, CFangleX,
    #                                                                         accAngX1, CFangleX1, pid))
