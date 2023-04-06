import RPi.GPIO as GPIO
import time
import numpy as np
import math

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
#steppinb=33
#dirpinb=31
#enpinb=29
#steppinc=40
#dirpinc=38
#enpinc=36
#----------b-----------
GPIO.setup(29,GPIO.OUT)
GPIO.setup(31,GPIO.OUT)
GPIO.setup(33,GPIO.OUT)
GPIO.output(33,0)
#------------c-----------
GPIO.setup(36,GPIO.OUT)
GPIO.setup(38,GPIO.OUT)
GPIO.setup(40,GPIO.OUT)
GPIO.output(40,0)
#---------------------input-----------------------------------------
print("input inverse parameter\n")
print("x:")
nX= raw_input()
nX=float(nX)
print("Y:")
nY=raw_input()
nY=float(nY)
#-------------------data---------------------------
L1=38
L2=27
ith1=-45
ith3=90
T1= 77 /15
T2= 63 /15
#------------------ inverse equ--------------------
if nX==8 and nY==8:
    thet1 =45
    thet3 =0

else:   
    X = (nX-1)*5 +2.5
    Y = (nY-1)*5+2.5
    X= X+13
    Y= Y+ 9
    r= ((X*X)+(Y*Y)-(L1*L1)-(L2*L2))/(2*L1*L2)
    
    th3= - math.acos(r)
    th1 = math.atan(Y/X) + math.atan(L2*math.sin(th3)/(L1+L2*math.cos(th3)))
    thet1 =math.degrees(th1)
    thet3 = - math.degrees(th3)
#------------------ value from intial position -------------------

thet1=thet1-ith1
thet3 = thet3 -ith3

#------------------ print value -------------------
print("theta1:")
print(thet1)
print("\n")

print("theta3:")
print(thet3)
print("\n")
r1= thet1 * 800 * T1/ 360
r1=int(r1)
r2 = thet3 * 800 *T2/ 360
r2=int(r2)
print(r1)
print(r2)

while True:
#---------b------------
  GPIO.output(31,GPIO.HIGH)
  for i in range(r1):
      GPIO.output(33,1)
      time.sleep(0.0005)
      GPIO.output(33,0)
      time.sleep(0.0005)
  time.sleep(2)
  GPIO.output(33,1)
#----------c-------------   
  GPIO.output(38,GPIO.HIGH)
  for i in range(r2):
      GPIO.output(40,1)
      time.sleep(0.0005)
      GPIO.output(40,0)
      time.sleep(0.0005)
  time.sleep(2)
  GPIO.output(40,1)
  break
GPIO.cleanup()
