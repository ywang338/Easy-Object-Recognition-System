import numpy as np
np.set_printoptions(threshold=np.nan)
import cv2
import math
import matplotlib.pyplot as plt

def p7(image, hough_image, hough_thresh):
    # image = cv2.imread(image)
    # hough_image = cv2.imread(hough_image)

    lines = []
    for i in range(len(hough_image)):
        for j in range(len(hough_image[0])):
            if hough_image[i, j, 0]> hough_thresh:
                lines.append((i, j))

    # for i in range(0,len(lines)-1):
    #     if abs(lines[i+1][0]-lines[i+1][0])<=0 and abs(lines[i+1][1]-lines[i+1][1])<=0:
    #         lines[i+1]=lines[i]


    for line in lines:
        rho = line[0]
        theta = np.pi * (line[1]) / 180+0.0001
        if (theta < (np.pi / 4.)) or (theta > (3. * np.pi / 4.0)):
            pt1 = (int(rho / np.cos(theta)), 0)
            pt2 = (int((rho - image.shape[0] * np.sin(theta)) / np.cos(theta)), image.shape[0])
            cv2.line(image, pt1, pt2, (255))
        else:
            pt1 = (0, int(rho / np.sin(theta)))
            pt2 = (image.shape[1], int((rho - image.shape[1] * np.cos(theta)) / np.sin(theta)))
            cv2.line(image, pt1, pt2, (255))
    return image

