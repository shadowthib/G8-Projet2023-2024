import time
import PCA9685 as PCA

class Servo():
    def __init__(self, min_pulse=350, max_pulse=550):
        self.pwm = PCA.PWM()
        self.pwm.frequency = 60
        self.min_pulse = min_pulse
        self.max_pulse = max_pulse

    def set_angle(self, angle):
        angle = max(-25, min(65, angle))
        pulse_width = self.min_pulse + ((angle) / 90.0) * (self.max_pulse - self.min_pulse)
        self.pwm.write(0, 0, int(pulse_width))

    def reset(self):
        self.set_angle(45)  # Set servo to 0 degree position


    def stop(self):
        self.pwm.write(0, 0, 0)


def test():

    while 1:
        servo = Servo()
        angle = int(input("Enter an angle:"))

        if angle == 69:
            break
        else:
            servo.set_angle(angle)
            time.sleep(2)
            servo.set_angle(0)
            servo.stop()


test()




