import cv2

import numpy as np

def trans(img, tx, ty, same_dim = True):
    X, Y = img.shape
    img_new = np.zeros((X+tx,Y+ty), 'uint8')
    
    for x in range(X):
        for y in range(Y):
            img_new[x+tx,y+ty] = int(img[x,y])
    if same_dim:
        return img_new[:X, :Y]
    else:
        return img_new

def rot(img, th, centre = True):
    X, Y = img.shape
    img_new = np.zeros((X, Y), 'uint8')
    
    M = [[np.cos(th), -np.sin(th)], [np.sin(th), np.cos(th)]]
    
    if centre:
        midX = X/2 + 1
        midY = Y/2 + 1
        for x in range(X):
            for y in range(Y):
                [temp1, temp2] = np.dot(M, [x-midX,y-midY])
                temp1 = int(temp1) + midX
                temp2 = int(temp2) + midY
                if (temp1 >= 0 and temp1 < 256) and (temp2 >= 0 and temp2 < 256):
                    img_new[temp1, temp2] = img[x, y]
        
    else:
        for x in range(X):
            for y in range(Y):
                [temp1, temp2] = np.dot(M, [x,y])
                temp1 =int(temp1)
                temp2 = int(temp2)
                if (temp1 >= 0 and temp1 < 256) and (temp2 >= 0 and temp2 < 256):
                    img_new[temp1, temp2] = img[x, y]
    
    return img_new

def ref(img):
    X, Y = img.shape
    
    if X != Y:
        return 0
    
    img_new = np.zeros((X, Y), 'uint8')
    
    for x in range(X):
        for y in range(Y):
            img_new[y,x] = img[x,y]
    
    return img_new
    

def show(img):
    cv2.imshow('image',img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()