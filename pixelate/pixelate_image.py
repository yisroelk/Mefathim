from PIL import Image
import numpy as np

def pixelate(path, save_path):
    #open desired image
    im = Image.open(path)
    #find its width & height
    w,h = im.size
    #find NEW dimensions from user-defined number (50% for example)
    new_w = 10
    new_h = 10
    #downsample image to these new dimensions
    down_sampled = im.resize((new_w, new_h))
    #upsample back to original size (using "4" to signify bicubic)
    up_sampled = down_sampled.resize((w, h), resample = 4)
    #save the image
    up_sampled.save(save_path)

pixelate("/Users/yisroel/האחסון שלי/Mefathim/pixelate/collage_poster_shows_2.jpg","/Users/yisroel/האחסון שלי/Mefathim/pixelate/new_image.jpg")