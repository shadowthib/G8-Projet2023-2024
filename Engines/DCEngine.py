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

        GPIO.setmode(GPIO.BCM)
        for pin in self.pins:
            GPIO.setup(pin, GPIO.OUT)

    def motor_state(self, motorA, motorB, pwm_value):
        print('Motor A: {}, Motor B: {}'.format(motorA, motorB))
        GPIO.output(motorA , GPIO.HIGH if pwm_value > 0 else GPIO.LOW)
        GPIO.output(motorB , GPIO.HIGH if pwm_value < 0 else GPIO.LOW)
        #self.pwm.write(self.en_1 if motorA == self.motor1_A else self.en_1, 0, abs(pwm_value))
        if motorA == self.motor1_A:
            self.pwm.write(self.en_1, 0, abs(pwm_value))
        else:
            self.pwm.write(self.en_2, 0, abs(pwm_value))

    def forward(self):
        print('Forward')
        self.motor_state(self.motor1_A, self.motor1_B, 4095)
        self.motor_state(self.motor2_A, self.motor2_B, 4095)

    def backward(self):
        print('Backward')
        self.motor_state(self.motor1_A, self.motor1_B, -4095)
        self.motor_state(self.motor2_A, self.motor2_B, -4095)

    def stop(self):
        print('Stop')
        self.motor_state(self.motor1_A, self.motor1_B, 0)
        self.motor_state(self.motor2_A, self.motor2_B, 0)





def test():

    motor = DCEngine()


    motor.forward()

    time.sleep(2)


    motor.backward()
    time.sleep(2)

    motor.stop()


test()

