import RPi.GPIO as gpio
import time 

e=11
d=13
s=15

gpio.setmode(gpio.BOARD)
gpio.setup(e,gpio.OUT)
gpio.setup(d,gpio.OUT)
gpio.setup(s,gpio.OUT)
gpio.output(e,1)

p=gpio.PWM(s,400)
def spinmotor(dir,num_step):
    
    gpio.output(e,0)
    gpio.output(d,dir)
    while num_step > 0:
    	p.start(1)
    	time.sleep(0.005)
    	num_step = int(num_step)-1
    p.stop()
    gpio.output(e,1)
    gpio.cleanup()
    return True
dir_input = raw_input("please enter o or c for open or close:")
num_step = raw_input("please enter the nuber of step:")
if dir_input == 'c':
    spinmotor(True,num_step)
else:
    spinmotor(False,num_step)

