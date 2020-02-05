import time


class PIDController:
    error_prior = 0
    integral = 0
    pid_value = 0

    def __init(self, kp, ki, kd, set_point):
        self.Kp = kp
        self.Ki = ki
        self.Kd = kd
        self.set_point = set_point

    def update_pid(self, error):
        return update(error, time.time())

    def update(self, error, dt):
        derivative = (error - errorPrior) / dt
        self.integral += error * dt
        self.error_prior = error
        self.pid_value = self.Kp * error + self.Ki * self.integral + self.Kd * derivative
        print("Integral = " + str(self.integral) + "\nError Prior = " +
              str(self.error_prior) + "\nValue = " + str(self.pid_value))
        return value

    def reset(self):
        self.error_prior = 0
        self.integral = 0
        self.pid_value = 0

    def get_set_point(self):
        return self.set_point
