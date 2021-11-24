# -*- coding: utf-8 -*-
"""
Created on Tue Nov 23 18:51:14 2021

@author: Necati
"""

import cv2
import math

vid = "D:\data_for_driverdrowsiness/1-FemaleNoGlasses.avi"
Folder = "./data"
cap = cv2.VideoCapture(vid)
Rate = cap.get(5) #rate
i=0
y=0
while(cap.isOpened()):
    frameId = cap.get(1) #choosen frame
    ret, frame = cap.read()
    if (ret != True):
        break
    if (frameId % math.floor(Rate) == 0):
        filename = Folder + "/video_" + str(y) + "_frame_" + str(i) + ".jpg"
        cv2.imwrite(filename, frame)
        i+=1
cap.release()
y+=1
i=0


