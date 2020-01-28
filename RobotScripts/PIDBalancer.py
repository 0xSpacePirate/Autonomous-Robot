import smbus
import math
import time
import simple_pid
import GyroFilter as gyroFilter

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


def dist(a, b):
    return math.sqrt((a * a) + (b * b))


def get_y_rotation(x, y, z):
    radians = math.atan2(x, dist(y, z))
    return -math.degrees(radians)


def get_x_rotation(x, y, z):
    radians = math.atan2(y, dist(x, z))
    return math.degrees(radians)


pid = simple_pid.PID(1.0, -0.04, 0.0, setpoint=0)

# time.sleep(time_diff - 0.005)  # SHOULDN'T IT BE AS SMALL AS POSSIBLE? - TEST

(gyro_scaled_x, gyro_scaled_y, gyro_scaled_z, accel_scaled_x, accel_scaled_y, accel_scaled_z) = gyroFilter.read_all()

# The angle of the Gyroscope
gyroAngleX += gyro_scaled_x * time_diff
gyroAngleY += gyro_scaled_y * time_diff
gyroAngleZ += gyro_scaled_z * time_diff

# http://ozzmaker.com/2013/04/18/success-with-a-balancing-robot-using-a-raspberry-pi/
accAngX = (math.atan2(accel_scaled_x, accel_scaled_y) + M_PI) * RAD_TO_DEG
# math.atan2 numeric value between -PI and PI representing the angle theta of an (x, y) point.
CFangleX = K * (CFangleX + gyro_scaled_x * time_diff) + (1 - K) * accAngX

# http://blog.bitify.co.uk/2013/11/reading-data-from-mpu-6050-on-raspberry.html
accAngX1 = get_x_rotation(accel_scaled_x, accel_scaled_y, gyro_scaled_z)
# accAngX1 = get_x_rotation(accel_scaled_x, accel_scaled_y, gyro_scaled_x) or this one - test?

CFangleX1 = (K * (CFangleX1 + gyro_scaled_x * time_diff) + (1 - K) * accAngX1)

# Followed the Second example because it gives reasonable pid reading
p = pid(CFangleX1)


def get_pid_value():
    print("PID value = " + str(p))
    return p



#print(
#    "{0:.2f} {1:.2f} {2:.2f} {3:.2f} | {4:.2f} {5:.2f} | {}".format(gyroAngleX, gyroAngleY, accAngX, CFangleX,
#                                                                         accAngX1, CFangleX1, pid))
