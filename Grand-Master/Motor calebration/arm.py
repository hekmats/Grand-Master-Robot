import RPi.GPIO as gpio
import time
import numpy as np
import math 



xmove={"a":1,
       "b":2,
       "c":3,
       "d":4,
       "e":5,
       "f":6,
       "g":7,
       "h":8}



#--------init the inverse parameter---#
L1=40
L2=28
ith1=-45 #for th base
ith3=90  #for the elbow 
#--------------------------------------#

#-----------right_left_motor-----------#
e1=11
d1=13
s1=15
#--------------------------------------#
#-----------up_down_motor--------------#
e2=29
d2=31
s2=33
#--------------------------------------#
#-----------elbow_motor----------------#
e3=36
d3=38
s3=40
#--------------------------------------#
#-----------servo_motor----------------#
s4=12
#--------------------------------------#


gpio.setmode(gpio.BOARD)
gpio.setup(e1,gpio.OUT)
gpio.setup(e2,gpio.OUT)
gpio.setup(e3,gpio.OUT)

gpio.output(e1,1)
gpio.output(e2,1)
gpio.output(e2,1)


def updateboard(source, target, boardbefore):
	sourcex = xmove[source[0]]
	sourcey = 9-int(source[1])
	targetx = xmove[target[0]]
	targety = 9-int(target[1])
	print (boardbefore)
	boardbefore[targety][targetx] = boardbefore[sourcey][sourcex] 
	boardbefore[sourcey][sourcex] = "."	
	print (boardbefore)	
	return (boardbefore)



def speaker(text):
	cmd_beg= 'espeak -s100 '
	cmd_end= ' | aplay /home/pi/Desktop/Text.wav  2>/dev/null' # To play back the stored .wav file and to dump the std errors to /dev/null
	cmd_out= '--stdout > /home/pi/Desktop/Text.wav ' # To store the voice file
	text = text.replace(' ', '_')
	call([cmd_beg+cmd_out+text], shell=True)
	call(["aplay", "/home/pi/Desktop/Text.wav"])


def right_left_motor(dir,num_step):
        print('thet1:')
	print (num_step)
	#setup the pins for this motor as output#
	gpio.setup(d1,gpio.OUT)
	gpio.setup(s1,gpio.OUT)
	#gpio.output(e1,1)
	#definw the pwm for this motor #
	p=gpio.PWM(s1,400)
	gpio.output(e1,0)
	gpio.output(d1,dir)
	while num_step > 0:
		#print('mhd')
		p.start(1)
		time.sleep(0.005)
		num_step = int(num_step)-1
	p.stop()
	gpio.output(e1,1)
	#gpio.cleanup()
	return True


def up_down_motor(dir,num_step):
	#setup the pins for this motor as output#
	gpio.setup(d2,gpio.OUT)
	gpio.setup(s2,gpio.OUT)
	#gpio.output(e2,1)
	gpio.output(e2,0)
	gpio.output(d2,dir)
	for x in range(num_step):
		gpio.output(s2,1)
		time.sleep(0.00015)
		gpio.output(s2,0)
		time.sleep(0.00015)
	time.sleep(2)
	gpio.output(e2,1)
	#gpio.cleanup()
	return True

def elbow_motor(dir,num_step):
	#setup the pins for this motor as output#
        print("thet3")
        print(num_step)
	gpio.setup(d3,gpio.OUT)
	gpio.setup(s3,gpio.OUT)
	#gpio.output(e3,1)

	#definw the pwm for this motor #
	p=gpio.PWM(s3,300)

	gpio.output(e3,0)
	gpio.output(d3,dir)
	while num_step > 0:
		p.start(1)
		time.sleep(0.005)
		num_step = int(num_step)-1
	p.stop()
	gpio.output(e3,1)
	#gpio.cleanup()
	return True

def servo_motor(move):
	#setup the pins for this motor as output#
	gpio.setup(s4,gpio.OUT)

	#definw the pwm for this motor #
	pwm=gpio.PWM(s4,50)
	pwm.start(0)
	if move == True:
		pwm.ChangeDutyCycle(5)
	else:
		pwm.ChangeDutyCycle(0)
        pwm.stop()
        #gpio.cleanup()
	return True



#----------change the letter of move to number-----#
def convert(source,target):
	global sourcex ,sourcey,targetx,targety,pos
	sourcey = xmove[source[0]]
	sourcex = 9-int(source[1])
	targety = xmove[target[0]]
	targetx = 9-int(target[1])

	print(sourcex)
	print(sourcey)
	print(targetx)
	print(targety)
	return True

#-----------get the inverse for the source postion the arm--------#
def inverse_source():
	global ith1,ith3
	ith1=-45 #for th base
	ith3=90  #for the elbow 
	if sourcex==8 and sourcey==8:
		curent1 = 37.7
		current3 = 0
		#print(thet1)
		#print(thet3)

	else:
		X = (sourcex-1)*5 +2.5
		Y = (sourcey-1)*5 +2.5
		X= X+16
                Y= Y+2
		r= ((X*X)+(Y*Y)-(L1*L1)-(L2*L2))/(2*L1*L2)
		th3= math.acos(r)
		th1 = math.atan(Y/X) - math.atan(L2*math.sin(th3)/(L1+L2*math.cos(th3)))
		curent1 =math.degrees(th1)
		current3 = math.degrees(th3)
	thet1=curent1-ith1
	thet3 = current3 -ith3
	print(thet1)
	print(thet3)
	#---------------call right_left_motor------------------------#
	step1=abs(round((565*thet1)/90))
	if thet1 > 0:
		right_left_motor(False,step1)
	else:
		right_left_motor(True,step1)
	#------------------------------------------------------------#

	#---------------call elbow_motor-----------------------------#
	step3=abs((575*thet3)/90)
	if thet3 > 0:
		elbow_motor(True,step3)
	else:
		elbow_motor(False,step3)
	#------------------------------------------------------------#
	ith1=curent1 #for th base
	ith3=current3 #for the elbow 


#-----------get the inverse for the target postion the arm--------#
def inverse_target():
	if targetx==8 and targety==8:
		thet1 = 45
		thet3 = 0
		print(thet1)
		print(thet3)


	else:
		X = (targetx-1)*4.5+2.5
		Y = (targety-1)*4.5+2.5
		X= X+16
		Y= Y + 12
		r= ((X*X)+(Y*Y)-(L1*L1)-(L2*L2))/(2*L1*L2)
		th3= math.acos(r)
		th1 = math.atan(Y/X) - math.atan(L2*math.sin(th3)/(L1+L2*math.cos(th3)))
		curent1 =math.degrees(th1)
		current3 = math.degrees(th3)
	thet1=curent1-ith1
	thet3 = current3 -ith3
	print(thet1)
	print(thet3)
	#---------------call right_left_motor------------------------#
	step1=abs(round((565*thet1)/90))
	if thet1 > 0:
		elbow_motor(False,step1)
	else:
		elbow_motor(True,step1)
	#------------------------------------------------------------#

	#---------------call elbow_motor-----------------------------#
	step3=abs((575*thet3)/90)
	if thet1 > 0:
		right_left_motor(False,step1)
	else:
		right_left_motor(True,step1)
	#------------------------------------------------------------#
	#ith1=-45 #for th base
	#ith3=90  #for the elbow 




#def arm_move(source,target):
#	pos=convert(postion)

#dir_input = raw_input("please enter o or c for open or close for right and left motor:")
#num_step = raw_input("please enter the nuber of step:")
#if dir_input == 'c':
#    right_left_motor(True,num_step)
#else:
#    right_left_motor(False,num_step)

#dir_input_elbow = raw_input("please enter o or c for open or close for elbow:")
#num_step = raw_input("please enter the nuber of step:")
#if dir_input_elbow == 'c':
#    elbow_motor(True,num_step)
#else:
#    elbow_motor(False,num_step)
angel=raw_input('enter move')

convert(angel[0:2],angel[2:4])
inverse_source()
print("done")
#inverse_target()
print("all is done")
gpio.cleanup()



