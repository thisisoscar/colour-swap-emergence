''' Much quicker but looses quality, especially when colours are similar.
    Doesn't destroy the computer and force it to stop compiling which is good I guess.
    Saves as image_to_video.avi
'''

import cv2
import os
from stopwatch.new_stopwatch import Stopwatch
import pyautogui as pg
from random import randint
from time import sleep
Each_Time = Stopwatch()
Total_Time = Stopwatch()
 
width = 1440
hieght = 900
 
fps = 10
 
fourcc = cv2.VideoWriter_fourcc(*'MP42')
 
video = cv2.VideoWriter('image_to_video.avi', fourcc, float(fps), (width, hieght))

directry = input('Enter the directory for the file to be added to: ')
 
img_name_list = os.listdir(directry)

Total_Time.start()
for frame_count in range(2001):
    Each_Time.start()
    
    img_name = f'{frame_count}.jpg'
    img_path = os.path.join(directry, img_name)
    img = cv2.imread(img_path)
    img_resize = cv2.resize(img, (width, hieght))
     
    video.write(img_resize)

    try:
        print(frame_count, Each_Time.read(), Total_Time.read('mins'), 'time left:', ( (Total_Time.read('mins') / frame_count) * (5000 - frame_count) ), 'mins')
    except ZeroDivisionError:
        pass
    pg.move(randint(-1, 1), randint(-1, 1))
    sleep(1)
     
video.release()
