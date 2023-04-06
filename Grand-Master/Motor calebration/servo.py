import RPi.GPIO as gpio
import time

gpio.setmode(gpio.BOARD)

s=12

gpio.setup(s,gpio.OUT)
pwm=gpio.PWM(s,50)
pwm.start(0)
def spinmotor(move):
    #pwm.ChangeDutyCycle(move)
    pwm.ChangeDutyCycle(move)
    stop=raw_input('when you want to close press s then enter:')
    if stop == 's' :
        pwm.stop()
        gpio.cleanup()
    


number_of_step = int(raw_input('enter the number of step:'))
spinmotor(number_of_step)


