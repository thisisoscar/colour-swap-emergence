''' Much longer time but higher quality, especially when colours are similar.
    Known to overcook the computer and slow it down to a halt and forced reset.
    Saves as video.mp4
'''

from moviepy.editor import *

import pyautogui as pg
from random import randint as r
import threading
from stopwatch.new_stopwatch import Stopwatch
from time import sleep

def stop_sleep():
    while True:
        pg.move(r(-1, 1), r(-1, 1))
        sleep(60)

t = threading.Thread(target=stop_sleep)
t.start()
S = Stopwatch()
S.start()

files = []
for i in range(5000):
    files.append(f'{i}.jpg')

clip = ImageSequenceClip(files, fps = 10) 
clip.write_videofile("video.mp4")

t.join()
S.read()
