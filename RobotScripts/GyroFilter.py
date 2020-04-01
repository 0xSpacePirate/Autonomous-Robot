# !/usr/bin/python

import smbus
import math
import time


class GyroFilter:

    def __init__(self):
        # Power management registers
        self.power_mgmt_1 = 0x6b
        self.power_mgmt_2 = 0x6c
        self.gyro_scale = 131.0
        self.accel_scale = 16384.0
        self.address = 0x68  # This is the address value read via the i2cdetect command
        self.bus = smbus.SMBus(1)  # or bus = smbus.SMBus(1) for Revision 2 boards

        self.gyro_vertical_center_x = 5.7
        self.gyro_vertical_center_y = 7.052

        # self.gyro_left_center_x = 6.09
        # self.gyro_left_center_y = 5.946

        # self.gyro_right_center_x = 5.378
        # self.gyro_right_center_y = 5.946

        self.accel_vertical_center_x = 0.013  # -0.173 default
        self.accel_vertical_center_y = 0.05
        self.accel_vertical_center_z = 1.07
        # self.accel_left_center_x = -0.64
        # self.accel_left_center_y = 0.122
        # self.accel_left_center_z = 0.829

        # self.accel_right_center_x = 0.66
        # self.accel_right_center_y = 0.04
        # self.accel_right_center_z = 0.848

        # Now wake the 6050 up as it starts in sleep mode
        self.bus.write_byte_data(self.address, self.power_mgmt_1, 0)
        self.now = time.time()
        self.K = 0.98
        self.K1 = 1 - self.K
        self.time_diff = 0.01
        (self.gyro_scaled_x, self.gyro_scaled_y, self.gyro_scaled_z, self.accel_scaled_x,
         self.accel_scaled_y, self.accel_scaled_z) = self.read_all()

    def read_all(self):
        raw_gyro_data = self.bus.read_i2c_block_data(self.address, 0x43, 6)
        raw_accel_data = self.bus.read_i2c_block_data(self.address, 0x3b, 6)
        gyro_scaled_x = self.twos_compliment((raw_gyro_data[0] << 8) + raw_gyro_data[1]) / self.gyro_scale
        gyro_scaled_y = self.twos_compliment((raw_gyro_data[2] << 8) + raw_gyro_data[3]) / self.gyro_scale
        gyro_scaled_z = self.twos_compliment((raw_gyro_data[4] << 8) + raw_gyro_data[5]) / self.gyro_scale
        accel_scaled_x = self.twos_compliment((raw_accel_data[0] << 8) + raw_accel_data[1]) / self.accel_scale
        accel_scaled_y = self.twos_compliment((raw_accel_data[2] << 8) + raw_accel_data[3]) / self.accel_scale
        accel_scaled_z = self.twos_compliment((raw_accel_data[4] << 8) + raw_accel_data[5]) / self.accel_scale
        return gyro_scaled_x, gyro_scaled_y, gyro_scaled_z, accel_scaled_x, accel_scaled_y, accel_scaled_z

    def twos_compliment(self, val):
        if val >= 0x8000:
            return -((65535 - val) + 1)
        else:
            return val

    def di2st(self, a, b):
        return math.sqrt((a * a) + (b * b))

    def get_y_rotation(self, x, y, z):
        radians = math.atan2(x, self.dist(y, z))
        return -math.degrees(radians)

    def get_x_rotation(self, x, y, z):
        radians = math.atan2(y, self.dist(x, z))
        return math.degrees(radians)

    def print_all(self):
        (self.gyro_scaled_x, self.gyro_scaled_y, self.gyro_scaled_z, self.accel_scaled_x,
         self.accel_scaled_y, self.accel_scaled_z) = self.read_all()
        print(
            "Time: {0:.4f} | GyroX: {1:.2f} | GyroY: {2:.2f} | GyroZ: {3:.2f} | AccelX: {4:.2f} | AccelY: {5:.2f} | "
            "AccelZ: {6:.2f}".format(time.time() - self.now, self.gyro_scaled_x, self.gyro_scaled_y, self.gyro_scaled_z,
                                     self.accel_scaled_x, self.accel_scaled_y, self.accel_scaled_z))

        last_x = self.get_x_rotation(self.accel_scaled_x, self.accel_scaled_y, self.accel_scaled_z)
        last_y = self.get_y_rotation(self.accel_scaled_x, self.accel_scaled_y, self.accel_scaled_z)
        gyro_offset_x = self.gyro_scaled_x
        gyro_offset_y = self.gyro_scaled_y
        gyro_total_x = (last_x) - gyro_offset_x
        gyro_total_y = (last_y) - gyro_offset_y

        # TODO remove commented code below?
        # print("{0:.4f} {1:.2f} {2:.2f} {3:.2f} {4:.2f} {5:.2f} {6:.2f}".format(time.time() - now, (last_x),
        # gyro_total_x, (last_x),(last_y), gyro_total_y, (last_y))) (gyro_scaled_x, gyro_scaled_y, gyro_scaled_z,
        # accel_scaled_x, accel_scaled_y, accel_scaled_z) = self.read_all() gyro_scaled_x -= gyro_offset_x
        # gyro_scaled_y -= gyro_offset_y gyro_x_delta = (gyro_scaled_x * self.time_diff) gyro_y_delta = (
        # gyro_scaled_y * self.time_diff) gyro_total_x += gyro_x_delta gyro_total_y += gyro_y_delta rotation_x =
        # self.get_x_rotation(accel_scaled_x, accel_scaled_y, accel_scaled_z) rotation_y = self.get_y_rotation(
        # accel_scaled_x, accel_scaled_y, accel_scaled_z)

        # last_x = self.K * (last_x + gyro_x_delta) + (self.K1 * rotation_x)
        # last_y = self.K * (last_y + gyro_y_delta) + (self.K1 * rotation_y)
        # print("{0:.4f} {1:.2f} {2:.2f} {3:.2f} {4:.2f} {5:.2f} {6:.2f}".format(time.time() - now, (rotation_x),
        # (gyro_total_x), (last_x),(rotation_y), (gyro_total_y),(last_y)))

    def calc_xy_values(self):
        RAD_TO_DEG = 57.29578
        # Get the deviations from our baseline
        x_diff = self.accel_scaled_x - self.accel_vertical_center_x
        y_diff = self.accel_scaled_y - self.accel_vertical_center_y
        z_diff = self.accel_scaled_z - self.accel_vertical_center_z

        # Work out the squares
        x = math.pow(x_diff, 2)
        y = math.pow(y_diff, 2)
        z = math.pow(z_diff, 2)

        # X Axis
        result = math.sqrt(x + z)
        result = x / result
        accel_angle_x = math.atan(result) * RAD_TO_DEG  # math.atan() output is in RAD

        # Y Axis
        result = math.sqrt(x + z)
        result = y / result
        accel_angle_y = math.atan(result) * RAD_TO_DEG

        return accel_angle_x, accel_angle_y

    def get_accel_center_xyz(self):
        return self.accel_vertical_center_x, self.accel_vertical_center_y, self.accel_vertical_center_z

    def get_current_xyz(self):
        return self.accel_scaled_x, self.accel_scaled_y, self.accel_scaled_z

    def get_gyro_and_accel(self):
        return self.gyro_scaled_x, self.gyro_scaled_y, self.gyro_scaled_z, self.accel_scaled_x, self.accel_scaled_y, self.accel_scaled_z

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

#
