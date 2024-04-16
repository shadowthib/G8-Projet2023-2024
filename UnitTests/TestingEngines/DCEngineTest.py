import RPi.GPIO as GPIO
import time

motor1 = 17
motor1Back = 18

motor2 = 27
motor2Back = 22



# Setup GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(motor1, GPIO.OUT)
GPIO.setup(motor1Back, GPIO.OUT)

GPIO.setup(motor2, GPIO.OUT)
GPIO.setup(motor2Back, GPIO.OUT)

def test_forward_movement():
    print("Testing forward movement...")
    GPIO.output(motor1, GPIO.HIGH)
    GPIO.output(motor1Back, GPIO.LOW)

    GPIO.output(motor2, GPIO.HIGH)
    GPIO.output(motor2Back, GPIO.LOW)
    time.sleep(2)

def test_reverse_movement():
    print("Testing reverse movement...")
    GPIO.output(motor1, GPIO.LOW)
    GPIO.output(motor1Back, GPIO.HIGH)

    GPIO.output(motor1Back, GPIO.HIGH)
    GPIO.output(motor2Back, GPIO.LOW)

    time.sleep(2)

# Run tests
test_forward_movement()
test_reverse_movement()

# Cleanup GPIO
GPIO.cleanup()
