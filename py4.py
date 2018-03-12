import cv2
import numpy as np

from py1 import p1
from py2 import p2
from py3 import p3

def p4(labels_in, database_in): # return overlays_out

    dict,label_with_direction = p3(labels_in);

    for i in dict:
        for j in database_in:
            if abs(dict[i]['roundness']-database_in[j]['roundness'])<=0.15:
                cv2.circle(labels_in, (dict[i]['position'][0], dict[i]['position'][1]), 10, (0, 0, 0))
    return labels_in;

# img_1 = cv2.imread('New_labeled.pgm',0)
#
# img_2 = cv2.imread('many_objects_1.pgm',0)
#
# binary = p1(img_2,130)
#
# label_img = p2(binary)
#
# database,img_two=p3(img_1)
#
# img_final = p4(label_img,database)
#
# cv2.imwrite("New_with_dict_1.pgm",img_final)
#
# ###########for pic 2
#
# img_1 = cv2.imread('New_labeled.pgm',0)
#
# img_2 = cv2.imread('many_objects_2.pgm',0)
#
# binary = p1(img_2,130)
#
# label_img = p2(binary)
#
# database,img_two=p3(img_1)
#
# img_final = p4(label_img,database)
#
# cv2.imwrite("New_with_dict_2.pgm",img_final);