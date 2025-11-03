import cv2 as cv
import numpy as np
blank=np.zeros((500,500,3), dtype='uint8')
#aplly to all the pixels
blank[:] =0,0,0
cv.imshow('blank image',blank)
#apply to specific spots
blank[0:0,500:500] =190,200,190
cv.imshow('blank image',blank)
rect=cv.rectangle(blank,(0,0),(250,250),(0,255,0),thickness=2)
cv.imshow('rectanglen image',rect)
cv.waitKey(0)