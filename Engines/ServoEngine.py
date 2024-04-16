from Engine import Engine

class Servo(Engine):
    def __init__(self, angle, pwm_control):
        self.angle = 0
        self.pwm_control = []