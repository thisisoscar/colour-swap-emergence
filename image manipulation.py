from PIL import Image
import pyautogui as pg
from stopwatch.new_stopwatch import Stopwatch
import random
import PIL
import comming as c
pg.FAILSAFE = False

T = Stopwatch()
Q = Stopwatch()
T.start()

im = Image.open('0.jpg')
width = im.size[0]
height = im.size[1]
im = im.convert('RGB')

print(im.mode)
im.show()
iteration = 0
# how many images
for _ in range(1, 2001):
    iteration += 1
    Q.start()
    for x in range(0, width-1):
        for y in range(0, height-1):
            thispx = im.getpixel((x, y))
            thispx = (thispx[0] + thispx[1] + thispx[2]) / 3

            # finding the average RGB colour of the above pixel and
            # calculating the difference between the selected pixel in the loop
            uppx = im.getpixel((x, y+1))
            uppx = (uppx[0] + uppx[1] + uppx[2]) / 3
            uppxdiff = abs(uppx-thispx)

            rightpx = im.getpixel((x+1, y))
            rightpx = (rightpx[0] + rightpx[1] + rightpx[2]) / 3
            rightpxdiff = abs(rightpx-thispx)

            downpx = im.getpixel((x, y-1))
            downpx = (downpx[0] + downpx[1] + downpx[2]) / 3
            downpxdiff = abs(downpx-thispx)

            leftpx = im.getpixel((x-1, y))
            leftpx = (leftpx[0] + leftpx[1] + leftpx[2]) / 3
            leftpxdiff = abs(leftpx-thispx)

            # finding the most different pixel out of all its neighbours
            biggest = max([uppxdiff, rightpxdiff, downpxdiff, leftpxdiff])
            thisRGB = im.getpixel((x, y))
            
            if biggest == uppxdiff:
                upRGB = im.getpixel((x, y+1))

                im.putpixel((x, y), (upRGB[0], upRGB[1], upRGB[2]))
                im.putpixel((x, y+1), (thisRGB[0], thisRGB[1], thisRGB[2]))

            elif biggest == rightpxdiff:
                rightRGB = im.getpixel((x+1, y))

                im.putpixel((x, y), (rightRGB[0], rightRGB[1], rightRGB[2]))
                im.putpixel((x+1, y), (thisRGB[0], thisRGB[1], thisRGB[2]))

            elif biggest == downpxdiff:
                downRGB = im.getpixel((x, y-1))

                im.putpixel((x, y), (downRGB[0], downRGB[1], downRGB[2]))
                im.putpixel((x, y-1), (thisRGB[0], thisRGB[1], thisRGB[2]))

            elif biggest == leftpxdiff:
                leftRGB = im.getpixel((x-1, y))

                im.putpixel((x, y), (leftRGB[0], leftRGB[1], leftRGB[2]))
                im.putpixel((x-1, y), (thisRGB[0], thisRGB[1], thisRGB[2]))

            #print(thispx)
    print(_)
    print(Q.read())
    print(T.concatenated_read())
    # find average from previous 8 instead of all-time as turning it off for 1000 seconds will dramatically change the projected time when it shouldn't. You can use try except index error. If excepts, faf around with the len of a list holding all the times in minutes
    print('expected to be finished in', c.commafy((T.read('mins') / iteration) * (5000 - iteration)), 'minutes')
    print()
    pg.move(random.randint(-1, 1), 0)
    #im.show()
    im.save(f'{_}.jpg')
print(T.read())
#im.show()

import video_fast_compiler
import video_slow_compiler
