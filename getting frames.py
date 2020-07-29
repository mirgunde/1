# -*- coding: utf-8 -*-
"""
Created on Mon Jul 27 20:10:37 2020

@author: Dell
"""

import cv2
import os, time
cam= cv2.VideoCapture("your path ")
#import numpy as np

try:
    if not os.path.exists('data'):
        os.makedirs('data')
        
except OSError:
    print("error in creating of data directory")
    
cf=0

while(True):
    
    ret, fr= cam.read()
    
    if ret:
        name= './data/frame'+ str(cf)+'.jpg'
        print("creating.."+name)
        cv2.imwrite(name, fr)
        cf+=1
    else:
        break
cam.release()
cv2.destroyAllWindows

