import cv2
import numpy as np
from py1 import p1
from py2 import p2
from py3 import p3
from py4 import p4


####    Part 1

gray_in = cv2.imread('two_objects.pgm',0)

binary_in = p1(gray_in, 125)

cv2.imwrite('New_two_objects.pgm',binary_in,(cv2.IMWRITE_PXM_BINARY, 0));

####    Part 2

image = cv2.imread("New_two_objects.pgm", 0)

label_img = p2(image);

cv2.imwrite('New_labeled.pgm',label_img,(cv2.IMWRITE_PXM_BINARY, 0));

####    Part 3

image = cv2.imread("New_labeled.pgm", 0)
dicts,image=p3(image);
for i in dicts:
    cv2.circle(image, (dicts[i]['position'][0], dicts[i]['position'][1]), 10, (0, 0, 255))
    cv2.line(image, (dicts[i]['position'][0], dicts[i]['position'][1]),(dicts[i]['position'][0] + 20, dicts[i]['position'][1] + int(np.tan(dicts[i]['orientation']) * 20)),(255, 255, 255))

cv2.imwrite("New_with_dict.pgm",image);

####    Part 4
img_1 = cv2.imread('New_labeled.pgm',0)

img_2 = cv2.imread('many_objects_1.pgm',0)

binary = p1(img_2,130)

label_img = p2(binary)

database,img_two=p3(img_1)

img_final = p4(label_img,database)

cv2.imwrite("New_with_dict_1.pgm",img_final)

###########for pic 2

img_1 = cv2.imread('New_labeled.pgm',0)

img_2 = cv2.imread('many_objects_2.pgm',0)

binary = p1(img_2,130)

label_img = p2(binary)

database,img_two=p3(img_1)

img_final = p4(label_img,database)

cv2.imwrite("New_with_dict_2.pgm",img_final);