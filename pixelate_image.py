from PIL import Image

def pixelate(path, save_path):
    #open desired image
    im = Image.open(path)
    #find its width & height
    w,h = im.size
    #find NEW dimensions from user-defined number (50% for example)
    new_w = 3
    new_h = 3
    #downsample image to these new dimensions
    down_sampled = im.resize((new_w, new_h))
    #upsample back to original size (using "4" to signify bicubic)
    up_sampled = down_sampled.resize((w, h), resample = 4)
    #save the image
    up_sampled.save(save_path)

pixelate("collage_poster_shows_2.jpg","new_image.jpg")