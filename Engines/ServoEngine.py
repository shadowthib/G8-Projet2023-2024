import time
import PCA9685 as PCA

class Servo():
    def __init__(self, min_pulse=350, max_pulse=550):
        self.pwm = PCA.PWM()
        self.pwm.frequency = 60
        self.min_pulse = min_pulse
        self.max_pulse = max_pulse
        self.angle = 20

    def set_angle(self, angle):
        print(angle)
        angle = max(-25, min(65, angle))
        pulse_width = self.min_pulse + ((angle) / 90.0) * (self.max_pulse - self.min_pulse)
        self.pwm.write(0, 0, int(pulse_width))

    def rotation_progression(self, sens):
        print(self.angle)
        '''while angle_start > -25 & angle_start <= 65:
            self.set_angle(angle)
            time.sleep(0.05)
            angle += 5

        # time.sleep(2)
        self.set_angle(20)
        self.stop()'''

    def reset(self):
        self.set_angle(45)


    def stop(self):
        self.pwm.write(0, 0, 0)


    def test(self):

        while 1:
            angle = int(input("Enter an angle:"))

            if angle == 69:
                break
            else:
                self.set_angle(angle)
                time.sleep(2)
                self.set_angle(0)
                self.stop()


    def mur1m(self, distance):
        angle = 20
        if distance > 15 and distance < 25:
            self.set_angle(20)

        elif distance > 25:
            if distance > 50:
                angle += 20
                self.set_angle(angle)
            else:
                angle -= 20
                self.set_angle(angle)
        elif distance < 15:
            angle += 20
            self.set_angle(angle)

    def bloquerRoueToutDroit(self):
        self.set_angle(20)

    def tour(self, distance):
        angle = 20
        if distance > 15 and distance < 25:
            self.set_angle(20)

        elif distance > 25:
            if distance > 40:
                angle -= 30
                self.set_angle(angle)
            else:
                angle -= 20
                self.set_angle(angle)
        elif distance < 15:
            angle += 20
            self.set_angle(angle)
