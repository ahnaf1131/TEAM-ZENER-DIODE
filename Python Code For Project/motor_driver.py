import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

servo_pin = 17
GPIO.setup(servo_pin, GPIO.OUT)

# Set up PWM on the GPIO pin
pwm = GPIO.PWM(servo_pin, 50)  # 50Hz frequency
pwm.start(0)  # Initialization

# Define GPIO pins for direction control
FORWARD_PIN = 18  # Pin for forward direction
BACKWARD_PIN = 23  # Pin for backward direction

# Set up GPIO
GPIO.setup(FORWARD_PIN, GPIO.OUT)
GPIO.setup(BACKWARD_PIN, GPIO.OUT)

# Initialize both pins to LOW
GPIO.output(FORWARD_PIN, GPIO.LOW)
GPIO.output(BACKWARD_PIN, GPIO.LOW)

direction = 'front'

def set_direction(direction):
    """Set the motor direction."""
    if direction == 'front':
        GPIO.output(FORWARD_PIN, GPIO.HIGH)
        GPIO.output(BACKWARD_PIN, GPIO.LOW)
    elif direction == 'back':
        GPIO.output(FORWARD_PIN, GPIO.LOW)
        GPIO.output(BACKWARD_PIN, GPIO.HIGH)

def set_speed(speed, pin_number):
    """Set the speed of the motor (0 to 100)."""
    if speed < 0:
        speed = 0
    elif speed > 100:
        speed = 100
    pin_number.ChangeDutyCycle(speed)
   	return speed

def set_angle(angle):
    duty = angle / 18 + 2
    GPIO.output(servoPIN, True)
    pwm.ChangeDutyCycle(duty)
    time.sleep(1)
    GPIO.output(servoPIN, False)
    pwm.ChangeDutyCycle(0)