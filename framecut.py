from random import randint as rand
import cv2 as cv
import math
import re
import os
import numpy as np

path = "../data"
folder_list = os.listdir(path)

for folder in folder_list:
    os.chdir(path+"/"+folder)
    file_list = os.listdir()


    for file in file_list:
        vid = cv.VideoCapture(file)
        vid.set(cv.CAP_PROP_FPS, 24)

        cv.VideoWriter()
        total_length = int(vid.get(cv.CAP_PROP_FRAME_COUNT))
        fps = vid.get(cv.CAP_PROP_FPS)
        for frame_num in range(0, total_length):
            vid.set(cv.CAP_PROP_POS_FRAMES, frame_num)
            flag, frame = vid.read()

            # resized_frame = cv.resize(frame, (width, height))

            cv.imwrite("frame/"+file + '%d.jpg' % frame_num, frame)
        print(file + " saved in")

        vid.release()
    cv.destroyAllWindows()

