import cv2
import numpy as np

def p2(binary_in):  # return labels_out
    shape = binary_in.shape
    a = np.zeros(shape, int);  # label matrix
    k = 1
    ls = []
    dic = {}
    group = 0 # label after equivalence

    for i in range(shape[0]):  # 1 is white o is background
        for j in range(shape[1]):
            if binary_in[i, j] == 0:  # background
                a[i, j] = 0;
            elif binary_in[i, j] == 255 and a[i - 1, j - 1] != 0:  # D is labeled
                a[i, j] = a[i - 1, j - 1];
            elif binary_in[i, j] == 255 and a[i - 1, j] == 0 and a[i, j - 1] == 0:  # B and C are not labeled
                a[i, j] = k;
                k += 1;  # update label
            elif binary_in[i, j] == 255 and a[i - 1, j] != 0 and a[i, j - 1] == 0:  # B is labeled
                a[i, j] = a[i - 1, j];
            elif binary_in[i, j] == 255 and a[i, j - 1] != 0 and a[i - 1, j] == 0:  # C is labeled
                a[i, j] = a[i, j - 1];
            elif a[i, j - 1] != 0 and a[i - 1, j] != 0:  # B and C are labeled
                if a[i, j - 1] == a[i - 1, j]:
                    a[i, j] = a[i, j - 1];
                else:
                    a[i, j] = a[i, j - 1];
                    ls.append([a[i-1,j],a[i,j-1]]) # save paired labels

    ls.sort()

    for k in range(len(ls)):  # Create Equivalence Table
        if (ls[k][0] in dic) and (ls[k][1] in dic):
            # if both labels are in dic, change the label to the smaller one
            # need to change all previous labels as well
            m = dic.get(ls[k][0])
            n = dic.get(ls[k][1])
            if (m < n):
                for i in dic:
                    if dic.get(i) == n:
                        dic[i] = m
            else:
                for i in dic:
                    if dic.get(i) == m:
                        dic[i] = n

        # if either one not in dic, add the same label to them
        if ls[k][0] in dic:
            dic[ls[k][1]] = dic.get(ls[k][0])
        if ls[k][1] in dic:
            dic[ls[k][0]] = dic.get(ls[k][1])
        # both not found, create new label
        else:
            group = group + 50
            dic[ls[k][0]] = group
            dic[ls[k][1]] = group
    row, col = a.shape
    pic = np.zeros([row, col])

    # give labels a specific value so they can be seen
    for i in range(0, row):
        for j in range(0, col):
            if (a[i, j] != 0):
                pic[i, j] = dic.get(a[i, j])
    return pic

# image = cv2.imread("New_two_objects.pgm", 0)
#
# label_img = p2(image);
#
# cv2.imwrite('New_labeled.pgm',label_img,(cv2.IMWRITE_PXM_BINARY, 0));