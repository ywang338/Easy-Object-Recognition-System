import numpy as np
np.set_printoptions(threshold=np.nan)
import cv2


def p5(image): #return edge_image_out

    #image = cv2.imread(image_in,0)
    row, col = image.shape

    a = np.zeros((row, col))
    b = np.zeros((row, col))
    out = np.zeros((row, col),np.uint8)

    sobel_x = [[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]]
    sobel_y = [[1, 2, 1], [0, 0, 0], [-1, -2, -1]]

    for i in range(1, row-1):
        for j in range(1, col-1):
            a[i, j] = (sobel_x * image[(i - 1):(i + 2), (j - 1):(j + 2)]).sum()
            b[i, j] = (sobel_y * image[(i - 1):(i + 2), (j - 1):(j + 2)]).sum()
            out[i, j] = abs(a[i, j]) + abs(b[i, j])


    return out

