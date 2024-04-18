import RPi.GPIO as GPIO
import time
import PCA9685 as PCA


class DCEngine:
    def __init__(self):
        self.motor1_A = 17
        self.motor1_B = 18
        self.motor2_A = 27
        self.motor2_B = 22

        self.en_1 = 5
        self.en_2 = 4

        self.pins = [self.motor1_A, self.motor1_B, self.motor2_A, self.motor2_B]

        self.pwm = PCA.PWM()
        self.pwm.frequency = 60

        self.speed = 4095

        GPIO.setmode(GPIO.BCM)
        for pin in self.pins:
            GPIO.setup(pin, GPIO.OUT)

    def motor_state(self, motorA, motorB, pwm_value):
        GPIO.output(motorA , GPIO.HIGH if pwm_value > 0 else GPIO.LOW)
        GPIO.output(motorB , GPIO.LOW if pwm_value > 0 else GPIO.HIGH)
        self.pwm.write(self.en_1 if motorA == self.motor1_A else self.en_2, 0, abs(pwm_value))

    def forward(self):
        self.motor_state(self.motor1_A, self.motor1_B, self.speed)
        self.motor_state(self.motor2_A, self.motor2_B, self.speed)

    def backward(self):
        self.motor_state(self.motor1_A, self.motor1_B, -self.speed)
        self.motor_state(self.motor2_A, self.motor2_B, -self.speed)

    def stop(self):
        self.motor_state(self.motor1_A, self.motor1_B, 0)
        self.motor_state(self.motor2_A, self.motor2_B, 0)





def test():

    motor= DCEngine()

    motor.speed = int(input("Enter a speed:"))

    motor.forward()
    time.sleep(2)

    motor.backward()
    time.sleep(2)

    motor.stop()

test()

