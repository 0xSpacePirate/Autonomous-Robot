import pigpio
import time
import math


class MyDataReader:

    def __init__(self):
        # some MPU6050 Registers and their Address
        self.PWR_MGMT_1 = 0x6B
        self.SMPLRT_DIV = 0x19
        self.CONFIG = 0x1A
        self.GYRO_CONFIG = 0x1B
        self.INT_ENABLE = 0x38
        self.ACCEL_XOUT_H = 0x3B
        self.ACCEL_YOUT_H = 0x3D
        self.ACCEL_ZOUT_H = 0x3F
        self.GYRO_XOUT_H = 0x43
        self.GYRO_YOUT_H = 0x45
        self.GYRO_ZOUT_H = 0x47
        self.TEMP_OUT_H = 0x41

        self.mpuAddress = 0x68  # MPU device address
        self.busNum = 1  # i2c bus number
        self.pi = pigpio.pi()  # connect to GPIO
        self.i2c = self.pi.i2c_open(self.busNum, self.mpuAddress, 0)  # open i2c and get handle
        self.mpuInit(self.pi, self.i2c)  # init MPU
        print(" Reading Data of Gyroscope and Accelerometer")

    def mpuInit(self, pi, i2c):
        pi.i2c_write_byte_data(i2c, self.SMPLRT_DIV, 7)  # write to sample rate register
        pi.i2c_write_byte_data(i2c, self.PWR_MGMT_1, 1)  # Write to power management register
        pi.i2c_write_byte_data(i2c, self.CONFIG, 0)  # Write to Configuration register
        pi.i2c_write_byte_data(i2c, self.GYRO_CONFIG, 24)  # Write to Gyro configuration register
        pi.i2c_write_byte_data(i2c, self.INT_ENABLE, 1)  # Write to interrupt enable register

    def readRawData(self, pi, i2c, address):
        # Accelero and Gyro value are 16-bit
        high = pi.i2c_read_byte_data(i2c, address)  # read high byte
        low = pi.i2c_read_byte_data(i2c, address + 1)  # read low byte
        # concatenate higher and lower value
        value = ((high << 8) | low)  # calculate 16-bit value
        # to get signed value from mpu6050
        if value > 32768:  value = value - 65536
        return value

    def calcAngles(self, ax, ay, az):
        xAngle = math.degrees(math.atan(ax / math.sqrt(ay * ay + az * az)))
        yAngle = math.degrees(math.atan(ay / math.sqrt(ax * ax + az * az)))
        return xAngle, yAngle, ax

    def get_xyx(self):
        # Read Accelerometer raw value
        acc_x = self.readRawData(self.pi, self.i2c, self.ACCEL_XOUT_H)
        acc_y = self.readRawData(self.pi, self.i2c, self.ACCEL_YOUT_H)
        acc_z = self.readRawData(self.pi, self.i2c, self.ACCEL_ZOUT_H)
        # Read Gyroscope raw value
        gyro_x = self.readRawData(self.pi, self.i2c, self.GYRO_XOUT_H)
        gyro_y = self.readRawData(self.pi, self.i2c, self.GYRO_YOUT_H)
        gyro_z = self.readRawData(self.pi, self.i2c, self.GYRO_ZOUT_H)
        # Full scale range +/- 250 degree/C as per sensitivity scale factor
        Ax = acc_x / 16384.0
        Ay = acc_y / 16384.0
        Az = acc_z / 16384.0

        Gx = gyro_x / 131.0
        Gy = gyro_y / 131.0
        Gz = gyro_z / 131.0

        temp = self.readRawData(self.pi, self.i2c, self.TEMP_OUT_H) / 340 + 36.53
        angles = self.calcAngles(Ax, Ay, Az)
        print("= = = = = = = = = = = = = = = = = = = = = =")
        print("X angle: {}\tY angle: {}\tX accel: {}".format(angles[0], angles[1], angles[2]))
        print("Gx=%.2f" % Gx, u'\u00b0' + "/s", "\tGy=%.2f" % Gy,
              u'\u00b0' + "/s", "\tGz=%.2f" % Gz, u'\u00b0' + "/s", "\tAx=%.2f g" % Ax,
              "\tAy=%.2f g" % Ay, "\tAz=%.2f g" % Az, "\tTemp=%.2f" % temp)
        return angles
