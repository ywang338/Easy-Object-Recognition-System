import numpy as np
np.set_printoptions(threshold=np.nan)
import cv2
import math

def p6(image, edge_thresh): # return [edge_thresh_image, hough_image]

    # image = cv2.imread(edge_image, 0)
    row, col = image.shape
    edge_thresh_out = np.zeros((row, col),np.uint8)

    for i in range(row):
        for j in range(col):
            if(image[i,j]<edge_thresh):
                edge_thresh_out[i, j]=0
            else:
                edge_thresh_out[i, j] = image[i, j]


    rho = int(math.sqrt(row*row*1.0+col*col*1.0))
    theta = 360
    accumulator = np.zeros((rho,theta),np.float32)

    for i in range(row):
        for j in range(col):
            if edge_thresh_out[i,j]!= 0:
                for k in range(theta):
                    rho = int(i*np.sin(2*np.pi*k/theta)+j*np.cos(2*np.pi*k/theta))
                    accumulator[rho,k]+=1

    return edge_thresh_out, accumulator


