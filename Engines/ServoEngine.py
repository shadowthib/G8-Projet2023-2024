import time
import PCA9685 as PCA

class Servo():
    def __init__(self, min_pulse=350, max_pulse=550):
        self._pwm = PCA.PWM()
        self._pwm.frequency = 60
        self._min_pulse = min_pulse
        self._max_pulse = max_pulse

        @property
        def pwm(self):
            return self._pwm
        
        @property
        def min_pulse(self):
            return self._min_pulse
        
        @property
        def max_pulse(self):
            return self._max_pulse
        
        @property
        def frequency(self):
            return self._pwm.frequency

    def set_angle(self, angle):
        angle = max(-25, min(65, angle))
        pulse_width = self.min_pulse + ((angle) / 90.0) * (self.max_pulse - self.min_pulse)
        self.pwm.write(0, 0, int(pulse_width))

    def reset(self):
        self.set_angle(45)  # Set servo to 0 degree position


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




