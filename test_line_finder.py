import numpy as np
np.set_printoptions(threshold=np.nan)
import cv2
import math
import matplotlib.pyplot as plt
from p5 import p5
from p6 import p6
from p7 import p7
from p8 import p8

####    Part 5

pic = cv2.imread('hough_simple_1.pgm',0)
pic = p5(pic)
cv2.imwrite("edge1.pgm", pic)

pic_1 = cv2.imread('hough_simple_2.pgm',0)
pic_1 = p5(pic_1)
cv2.imwrite("edge2.pgm", pic_1)

pic_2 = cv2.imread('hough_complex_1.pgm',0)
pic_2 = p5(pic_2)
cv2.imwrite("edge3.pgm", pic_2)

#### Part 6

pic = cv2.imread('edge1.pgm',0)
pic, houghOut = p6(pic,70)
cv2.imwrite("hough_simple_1_edge_threshed.pgm", pic)
cv2.imwrite("hough_image_1_result.pgm", houghOut)

pic = cv2.imread('edge2.pgm',0)
pic, houghOut = p6(pic,50)
cv2.imwrite("hough_simple_2_edge_threshed.pgm", pic)
cv2.imwrite("hough_image_2_result.pgm", houghOut)

pic = cv2.imread('edge3.pgm',0)
pic, houghOut = p6(pic,70)
cv2.imwrite("hough_simple_3_edge_threshed.pgm", pic)
cv2.imwrite("hough_image_3_result.pgm", houghOut)


####    Part 7
pic = cv2.imread('hough_image_1_result.pgm')
origin = cv2.imread('hough_simple_1.pgm')
pic = p7(origin,pic,250)
cv2.imwrite("hough1_lineImage.pgm", pic)

pic = cv2.imread('hough_image_2_result.pgm')
origin = cv2.imread('hough_simple_2.pgm')
pic = p7(origin,pic,250)
cv2.imwrite("hough2_lineImage.pgm", pic)

pic = cv2.imread('hough_image_3_result.pgm')
origin = cv2.imread('hough_complex_1.pgm')
pic = p7(origin,pic,150)
cv2.imwrite("hough3_lineImage.pgm", pic)

####    Part 8

pic = p8('hough_simple_1.pgm','hough_image_1_result.pgm','edge1.pgm',150)
cv2.imwrite("hough1_croppedLineImage.pgm", pic)
pic = p8('hough_simple_2.pgm','hough_image_2_result.pgm','edge2.pgm',140)
cv2.imwrite("hough2_croppedLineImage.pgm", pic)
pic = p8('hough_complex_1.pgm','hough_image_3_result.pgm','edge3.pgm',100)
cv2.imwrite("hough3_croppedLineImage.pgm", pic)
