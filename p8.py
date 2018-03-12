import numpy as np
np.set_printoptions(threshold=np.nan)
import cv2
import math
import matplotlib.pyplot as plt


def p8(image, hough_image, edge_thresh_image, hough_thresh):#return cropped_lines_image

    image = cv2.imread(image)
    hough_image = cv2.imread(hough_image)
    edge_thresh_image = cv2.imread(edge_thresh_image,0)

    ret, thresh1 = cv2.threshold(edge_thresh_image, 40, 255, cv2.THRESH_BINARY)
    row,col = edge_thresh_image.shape

    lines=[]
    step = 60
    for i in range(len(hough_image)):
        for j in range(len(hough_image[0])):
            if hough_image[i, j, 0]> hough_thresh:
                lines.append((i, j))
    for line in lines:
        rho = line[0]
        theta = np.pi * (line[1]) / 180+0.0001
        if (theta < (np.pi / 4.)) or (theta > (3. * np.pi / 4.0)):
            pt1 = (int(rho / np.cos(theta)), 0)
            pt2 = (int((rho - row * np.sin(theta)) / np.cos(theta)), row)

            if(pt1[0]>=640) or (pt2[0]>=640) or (pt1[0]<0) or (pt2[0]<0): continue
            steps1 = []
            steps1 = np.linspace(pt1[0], pt2[0]-1,num = step,endpoint=False)
            steps2 = []
            steps2 = np.linspace(0, row-1, num=step, endpoint=False)
            for i in range(len(steps1)-1):
                x = int(steps1[i])
                y = int(steps2[i])
                val1 = thresh1[y,x]
                x = int(steps1[i+1])
                y = int(steps2[i+1])
                val2 = thresh1[y,x]
                if val1==255 and val2==255:
                    cv2.line(image, (int(steps1[i]),int(steps2[i])), (int(steps1[i+1]),int(steps2[i+1])), (255))

        else:
            pt1 = (0, int(rho / np.sin(theta)))
            pt2 = (col, int((rho - col * np.cos(theta)) / np.sin(theta)))
            #cv2.line(image, pt1, pt2, (255))
            if (pt1[1] >= 640) or (pt2[1] >= 640) or (pt1[1] < 0) or (pt2[1] < 0): continue
            steps1 = []
            steps2 = []
            steps2 = np.linspace(pt1[1], pt2[1] - 1, num=step, endpoint=False)
            steps1 = np.linspace(0, col - 1, num=step, endpoint=False)
            for i in range(len(steps1) - 1):

                x = int(steps1[i])
                y = int(steps2[i])
                if (y > 479): continue
                val1 = thresh1[y, x]
                x = int(steps1[i + 1])
                y = int(steps2[i + 1])
                if (y > 479): continue
                val2 = thresh1[y, x]
                if val1 == 255 and val2 == 255:
                    cv2.line(image, (int(steps1[i]), int(steps2[i])), (int(steps1[i + 1]), int(steps2[i + 1])), (255))
    return image

