import random

import RPi.GPIO as GPIO
import time
import Engines.PCA9685 as PCA
import pick


class DCEngine:
    def __init__(self):
        self._motor1_A = 17
        self._motor1_B = 18
        self._motor2_A = 27
        self._motor2_B = 22

        self._en_1 = 5
        self._en_2 = 4

        self._pins = [self.motor1_A, self.motor1_B, self.motor2_A, self.motor2_B]

        self._pwm = PCA.PWM()
        self._pwm.frequency = 60

        @property
        def motor1_A(self):
            return self._motor1_A
        
        @property
        def motor1_B(self):
            return self._motor1_B
        
        @property
        def motor2_A(self):
            return self._motor2_A
        
        @property
        def motor2_B(self):
            return self._motor2_B
        
        @property
        def en_1(self):
            return self._en_1
        
        @property
        def en_2(self):
            return self._en_2
        
        @property
        def pins(self):
            return self._pins
        
        @property
        def get_pwm(self):
            return self._pwm
        
        @property
        def pwmfrequency(self):
            return self._pwm.frequency
        
        @pwm.setter
        def pwm(self, pwm):
            if isinstance(pwm, PCA.PWM):
                self._pwm = pwm

        @pwmfrequency.setter
        def pwmfrequency(self, frequency):
            if isinstance(frequency, int):
                self._pwm.frequency = frequency

        


        GPIO.setmode(GPIO.BCM)
        for pin in self.pins:
            GPIO.setup(pin, GPIO.OUT)

    def motor_state(self, motorA, motorB, pwm_value):
        print('Motor A: {}, Motor B: {}'.format(motorA, motorB))
        GPIO.output(motorA , GPIO.HIGH if pwm_value > 0 else GPIO.LOW)
        GPIO.output(motorB , GPIO.HIGH if pwm_value < 0 else GPIO.LOW)
        if motorA == self.motor1_A:
            self.pwm.write(self._en_1, 0, abs(pwm_value))
        else:
            self.pwm.write(self._en_2, 0, abs(pwm_value))

    def forward(self, speed_select, direction=None):
        print('Forward')
        if direction == "R":
            self.motor_state(self._motor1_A, self._motor1_B, speed_select)
        elif direction == "L":
            self.motor_state(self._motor2_A, self._motor2_B, speed_select)
        else :
            self.motor_state(self._motor1_A, self._motor1_B, speed_select)
            self.motor_state(self._motor2_A, self._motor2_B, speed_select)

    def backward(self, speed_select):
        print('Backward')
        self.motor_state(self._motor1_A, self._motor1_B, -speed_select)
        self.motor_state(self._motor2_A, self._motor2_B, -speed_select)

    def stop(self):
        print('Stop')
        self.motor_state(self._motor1_A, self._motor1_B, 0)
        self.motor_state(self._motor2_A, self._motor2_B, 0)


    def test_condition(self):


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
                self.forward(speed_select)
                time.sleep(1)
            if obstacle == 1:
                print("Obstacle détecté !")
                self.stop()
                direction = random.choice(['R', 'L'])
                self.forward(speed_select, direction)
                time.sleep(1)
                self.stop()
                break
            time.sleep(0.1)

        '''motor.backward(speed_select)
    
        time.sleep(2)'''


    def test_avance(self):
        speed_select = 4095

        while speed_select > 0:
            self.forward(speed_select)
            time.sleep(1)
            speed_select -= 500
        self.stop()

    def avancerReculer30cm(self):

        self.forward(round(4095*0.67))
        time.sleep(1)

        self.backward(round(4095*0.65))
        time.sleep(1)
        self.stop()


    def accelForward(self):
        speed_select = 0
        while speed_select < 4095:
            self.forward(speed_select)
            time.sleep(1)
            speed_select += 1000
        self.stop()

    def decelForward(self):
        speed_select = 4095
        while speed_select > 0:
            self.forward(speed_select)
            time.sleep(1)
            speed_select -= 1000
        self.stop()

