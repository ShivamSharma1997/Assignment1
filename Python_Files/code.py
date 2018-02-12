import cv2
import numpy as np

from utility import *

########################### DEFINING IF VARIABLES ###########################

tr = 0  #For Translation
ro = 1 #For Rotation
re = 0 #For Reflection

########################### READ AND PROCESS IMAGE ###########################

img = cv2.imread('../data/cameraman.tif')

img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

########################### FOR TRANSLATION ###########################

if tr:
    img_new = trans(img, 10, 20)

########################### FOR ROTATION ###########################

if ro:
    img_new = rot(img, np.pi/4)

########################### FOR REFLECTION ###########################

if re:
    img_new = ref(img)

########################### DISPLAYING PROCESSED IMAGE ###########################

show(img_new)