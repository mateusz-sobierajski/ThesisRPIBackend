import RPi.GPIO as GPIO
from time import sleep


def initGpio(ledpin):
    GPIO.setwarnings(False)  # disable warnings
    GPIO.setmode(GPIO.BOARD)  # set pin numbering system
    GPIO.setup(ledpin, GPIO.OUT)
    pwmPin = GPIO.PWM(ledpin, 1000)  # create PWM instance with frequency
    pwmPin.start(0)  # start PWM of required Duty Cycle
    return pwmPin


def gpioLED(pwmPin, value):
    pwmPin.ChangeDutyCycle(value)  # provide duty cycle in the range 0-100


('''
def gpioLED(value):
    ledpin = 16  # PWM pin connected to LED
    GPIO.setwarnings(False)  # disable warnings
    GPIO.setmode(GPIO.BOARD)  # set pin numbering system
    GPIO.setup(ledpin, GPIO.OUT)
    pi_pwm = GPIO.PWM(ledpin, 1000)  # create PWM instance with frequency
    pi_pwm.start(0)  # start PWM of required Duty Cycle
    try:
        while True:
            for duty in range(0, 101, 1):
                pi_pwm.ChangeDutyCycle(duty)  # provide duty cycle in the range 0-100
                sleep(0.01)
            sleep(0.5)

            for duty in range(100, -1, -1):
                pi_pwm.ChangeDutyCycle(duty)
                sleep(0.01)
            sleep(0.5)
    except KeyboardInterrupt:
        pass
    pi_pwm.stop()
    GPIO.cleanup()
''')