import RPi.GPIO as gpio
import time 

e=29
d=31
s=33

gpio.setmode(gpio.BOARD)
gpio.setup(e,gpio.OUT)
gpio.setup(d,gpio.OUT)
gpio.setup(s,gpio.OUT)
gpio.output(e,1)

def spinmotor(dir,num_step):
    gpio.output(e,0)
    gpio.output(d,dir)
    for x in range(num_step):
        gpio.output(s,1)
        time.sleep(0.00015)
        gpio.output(s,0)
        time.sleep(0.00015)
    time.sleep(2)
    gpio.output(e,1)
    gpio.cleanup()
        
dir_input = raw_input("please enter o or c for open or close:")
num_step = int(raw_input("please enter the nuber of step:"))
if dir_input == 'c':
    spinmotor(False,num_step)
else:
    spinmotor(True,num_step)