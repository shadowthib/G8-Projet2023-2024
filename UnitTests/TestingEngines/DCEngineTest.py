import RPi.GPIO as GPIO
import time
import PCA9685 as p
import board

motor1_A = 17
motor1_B = 18

motor2_A = 27
motor2_B = 22

EN_M0 = 4  # servo driver IC CH4
EN_M1 = 5  # servo driver IC CH5

pins = [motor1_A, motor1_B, motor2_A, motor2_B]

# Setup GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(motor1_A, GPIO.OUT)
GPIO.setup(motor1_B, GPIO.OUT)

GPIO.setup(motor2_A, GPIO.OUT)
GPIO.setup(motor2_B, GPIO.OUT)


def setSpeed(speed):
    speed *= 40
    print('speed is: ', speed)
    pwm.write(EN_M0, 0, speed)
    pwm.write(EN_M1, 0, speed)


def setup(busnum=None):
    global forward0, forward1, backward1, backward0
    global pwm
    if busnum == None:
        pwm = p.PWM()  # Initialize the servo controller.
    else:
        pwm = p.PWM(bus_number=busnum)  # Initialize the servo controller.

    pwm.frequency = 60
    forward0 = 'True'
    forward1 = 'True'
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)  # Number GPIOs by its physical location


def motor0(x):
    if x == 'True':
        GPIO.output(motor1_A, GPIO.LOW)
        GPIO.output(motor1_B, GPIO.HIGH)
    elif x == 'False':
        GPIO.output(motor1_A, GPIO.HIGH)
        GPIO.output(motor1_B, GPIO.LOW)
    else:
        print('Config Error')


def motor1(x):
    if x == 'True':
        GPIO.output(motor2_A, GPIO.LOW)
        GPIO.output(motor2_B, GPIO.HIGH)
    elif x == 'False':
        GPIO.output(motor2_A, GPIO.HIGH)
        GPIO.output(motor2_B, GPIO.LOW)


def forward():
    motor0(forward0)
    motor1(forward1)


def backward():
    motor0(backward0)
    motor1(backward1)


def forwardWithSpeed(spd=50):
    setSpeed(spd)
    motor0(forward0)
    motor1(forward1)


def backwardWithSpeed(spd=50):
    setSpeed(spd)
    motor0(backward0)
    motor1(backward1)


def stop():
    for pin in pins:
        GPIO.output(pin, GPIO.LOW)


def test_forward_movement():
    print("Testing forward movement...")
    GPIO.output(motor1_A, GPIO.HIGH)
    GPIO.output(motor1_B, GPIO.LOW)

    GPIO.output(motor2_A, GPIO.HIGH)
    GPIO.output(motor2_B, GPIO.LOW)
    time.sleep(2)


def test_reverse_movement():
    print("Testing reverse movement...")
    GPIO.output(motor1_A, GPIO.LOW)
    GPIO.output(motor1_B, GPIO.HIGH)

    GPIO.output(motor2_A, GPIO.HIGH)
    GPIO.output(motor2_B, GPIO.LOW)

    time.sleep(2)


# Run tests
test_forward_movement()
test_reverse_movement()

# Cleanup GPIO
GPIO.cleanup()
