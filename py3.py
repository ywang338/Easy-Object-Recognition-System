import cv2
import numpy as np
import math

def p3(label_img):  #return [database, output_image]
    labeled_img=label_img;
    a = np.unique(labeled_img);

    dicts = {}
    for i in range(len(a)-1):
        dicts[i] = {}

    # database_out = {}
    for h in range(len(a)-1): #get the position of the object
        area=0;x_mean=0;y_mean=0;
        for i in range(labeled_img.shape[0]):
            for j in range(labeled_img.shape[1]):
                if labeled_img[i,j]==a[h+1]:
                    area+=1;
                    y_mean+=i;
                    x_mean+=j;

        dicts[h]['position'] =[x_mean/area,y_mean/area]

    for h in range(len(a)-1): #get the orientation of the object
        xy_multi=0;x_second_moment=0;y_second_moment=0;
        for i in range(labeled_img.shape[0]):
            for j in range(labeled_img.shape[1]):
                if labeled_img[i,j]==a[h+1]:
                    xy_multi+=2*(i-dicts[h]['position'][1])*(j-dicts[h]['position'][0]);
                    y_second_moment+=(i-dicts[h]['position'][1])*(i-dicts[h]['position'][1]);
                    x_second_moment+=(j-dicts[h]['position'][0])*(j-dicts[h]['position'][0]);
        label = 0;
        # temp=float(xy_multi)/(x_second_moment-y_second_moment);
        theta=np.arctan2(xy_multi,(x_second_moment-y_second_moment))/2.0;
        temp_condition=(x_second_moment-y_second_moment)*math.cos(2*theta)+xy_multi*math.sin(2*theta)
        if temp_condition<0:
            theta=theta+np.pi/2;
            label=1;
        dicts[h]['orientation'] = theta;

        E_min = x_second_moment*math.sin(theta)*math.sin(theta)-xy_multi*math.sin(theta)*np.cos(theta)+y_second_moment*math.cos(theta)*math.cos(theta);
        if label==0:
            theta_temp=theta+math.pi/2;
        else:
            theta_temp = theta - np.pi / 2;
        E_max = x_second_moment*math.sin(theta_temp)*math.sin(theta_temp)-xy_multi*math.sin(theta_temp)*math.cos(theta_temp)+y_second_moment*math.cos(theta_temp)*math.cos(theta_temp);
        roundness =  E_min / E_max

        dicts[h]['roundness'] = roundness;


    for h in range(len(a)-1):
        max_dis=0;
        for i in range(labeled_img.shape[0]):
            for j in range(labeled_img.shape[1]):
                if labeled_img[i,j] == a[h+1]:
                    temp=np.sqrt((i-dicts[h]['position'][1])*(i-dicts[h]['position'][1])+(j-dicts[h]['position'][0])*(j-dicts[h]['position'][0]));
                    if max_dis<=temp:
                        max_dis=temp;

        dicts[h]['Template_size'] = max_dis;


    return dicts,labeled_img;

# image = cv2.imread("New_labeled.pgm", 0)
# dicts,image=p3(image);
# for i in dicts:
#     cv2.circle(image, (dicts[i]['position'][0], dicts[i]['position'][1]), 10, (0, 0, 255))
#     cv2.line(image, (dicts[i]['position'][0], dicts[i]['position'][1]),(dicts[i]['position'][0] + 20, dicts[i]['position'][1] + int(np.tan(dicts[i]['orientation']) * 20)),(255, 255, 255))
#
# cv2.imwrite("New_with_dict.pgm",image);
#
