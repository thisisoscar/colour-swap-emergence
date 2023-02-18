# colour-swap-emergence

image_manipulation is the file I should rename to main.py. It takes a jpeg image called 0.jpg and the code goes through each pixel calculating its average rgb colour value. It does the same with the pixels to its side and chooses the pixel with the largest difference. The colours of these pixels then switch so it looks like they move. After every pixel has been done, the new image that is created is saved as {n+1}.jpg. After enough iterations, it calls two video compilers to create the video that is created at 10 fps. If you want to use this, you need to manually set the number of iterations on all compilers and you might want to tweak some settings eg. different fps, only one compiler, output video type. I would put some of the videos in but they're too big

# fast compiler
Much quicker but looses quality, especially when colours are similar.
Doesn't destroy the computer and force it to stop compiling which is generally good.
Saves as image_to_video.avi.
Runs first

# slow compiler
Much longer time but higher quality, especially when colours are similar.
Sometimes force shuts down my computer and slow it down to a halt with many images.
Saves as video.mp4.
Runs second

# none of the above
If none of them work, you could use shutter encoder or something similar. I'm not sure about quality but it's faster than both and has more output types. The H.265 function worked for me and you need to activate the image sequence, you can set it to whatever fps you want there
