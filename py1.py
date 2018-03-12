import numpy as np
import cv2


def p1(gray_in, thresh_val): # return binary_out

    shape = gray_in.shape
    for i in range(shape[0]):
        for j in range(shape[1]):
            if gray_in[i,j] >= thresh_val:
                gray_in[i,j] = 255
            else:
                gray_in[i,j] = 0

    return gray_in
#
# gray_in = cv2.imread('/Users/ou/PycharmProjects/untitled/two_objects.pgm',0)
#
# binary_in = p1(gray_in, 125)
#
# cv2.imwrite('New_two_objects.pgm',binary_in,(cv2.IMWRITE_PXM_BINARY, 0));