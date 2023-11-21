from hal import hal_servo as servo
from hal import hal_adc as adc
from time import sleep

adc.init()
servo.init()

while True:
    value = adc.get_adc_value(1)
    servo.set_servo_position(value)
    print(value)
    sleep(0.1)