import time
from datetime import datetime


class PIDController:

    def __init__(self, kp, ki, kd, set_point):
        self.Kp = kp
        self.Ki = ki
        self.Kd = kd
        self.set_point = set_point
        self.error_prior = 0
        self.integral = 0
        self.pid_value = 0
        self.now = time.time()

    def update_pid(self, error):
        # return self.update(error, time.time())
        # return self.update(error, datetime.now().microsecond / MICROSECOND_TO_SECOND)
        return self.update(error, round(time.time() - self.now, 6))

    def update(self, error, dt):
        self.integral += error * dt
        derivative = (error - self.error_prior) / dt
        self.error_prior = error
        self.pid_value = self.Kp * error + self.Ki * self.integral + self.Kd * derivative
        print("Time = " + str(dt) +
              "\nIntegral = " + str(self.integral) +
              "\nError Prior = " + str(self.error_prior) +
              "\nValue = " + str(self.pid_value))
        self.update_time_frame()
        return self.pid_value

    def update_time_frame(self):
        self.now = time.time()

    def reset(self):
        self.error_prior = 0
        self.integral = 0
        self.pid_value = 0

    def get_pid(self):
        return float(self.pid_value)

    def get_set_point(self):
        return self.set_point
