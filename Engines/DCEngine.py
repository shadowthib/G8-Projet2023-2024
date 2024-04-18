import random

import RPi.GPIO as GPIO
import time
import PCA9685 as PCA
import pick
import math


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
        if motorA == self.motor1_A:
            self.pwm.write(self.en_1, 0, abs(pwm_value))
        else:
            self.pwm.write(self.en_2, 0, abs(pwm_value))

    def forward(self, speed_select, direction=None):
        print('Forward')
        if direction == "R":
            self.motor_state(self.motor1_A, self.motor1_B, speed_select)
        elif direction == "L":
            self.motor_state(self.motor2_A, self.motor2_B, speed_select)
        else :
            self.motor_state(self.motor1_A, self.motor1_B, speed_select)
            self.motor_state(self.motor2_A, self.motor2_B, speed_select)

    def backward(self, speed_select):
        print('Backward')
        self.motor_state(self.motor1_A, self.motor1_B, -speed_select)
        self.motor_state(self.motor2_A, self.motor2_B, -speed_select)

    def stop(self):
        print('Stop')
        self.motor_state(self.motor1_A, self.motor1_B, 0)
        self.motor_state(self.motor2_A, self.motor2_B, 0)


def test_condition():

    motor = DCEngine()

    while True:
        speed = int(input("Sélectionnez la vitesse : [1] Lent [2] Moyen [3] Rapide [4] Très rapide \n"))
        if speed >= 1 and speed <= 4:
            match speed :
                case 1 :
                    speed_select = 512
                    break
                case 2 :
                    speed_select = 1028
                    break
                case 3 :
                    speed_select = 2512
                    break
                case 4:
                    speed_select = 4095
                    break
        else :
            print("Inscrivez un nombre entre 1 et 4")


    while True:
        obstacle = random.randrange(0, 2)
        if obstacle == 0:
            motor.forward(speed_select)
            time.sleep(1)
        if obstacle == 1:
            print("Obstacle détecté !")
            motor.stop()
            direction = random.choice(['R', 'L'])
            motor.forward(speed_select, direction)
            time.sleep(1)
            motor.stop()
            break
        time.sleep(0.1)

    '''motor.backward(speed_select)

    time.sleep(2)'''


def test_avance():
    motor = DCEngine()
    speed_select = 4095

    while speed_select > 0:
        motor.forward(speed_select)
        time.sleep(1)
        speed_select -= 500
    motor.stop()

def avancerReculer30cm():
    motor = DCEngine()

    motor.forward(round(4095*0.67))
    time.sleep(1)

    motor.backward(round(4095*0.67))
    time.sleep(1)
    motor.stop()

#avancerReculer30cm()

#test_condition()
#test_avance()
