import cv2 as cv
import numpy as np 
print('bw')
def btow():
    im = cv.imread('/home/pi/mycode/image/2.jpg')
    print('btow')
    #print(im.shape)
    w ,h =im.shape[:2]
    center = (w // 2,h // 2)
    M = cv.getRotationMatrix2D(center,90,1.0)
    im = cv.warpAffine(im, M, (w, h))
    #print(w,h)
    #cv.imshow('hkm2',im)
    for x in range(w) :
    	for y in range(h):
    		#m=im[x,y]
    		(b,g,r) = im[x,y]
		#print (im[x,y])
		#print(b,g,r)
		if b<60 and r<60 and g<60:
			im[x,y] = [145,145,145]
    cv.imwrite('/home/pi/mycode/image/1.jpg',im)
    #return()
#cv.imshow('hkm',im)
#if cv.waitKey(0)==(27):
#	cv.destroyAllWindows()
#return()