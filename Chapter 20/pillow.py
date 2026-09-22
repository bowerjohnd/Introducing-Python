# interpreter example using PIL

from PIL import Image
import time

print('=' * 20)

img = Image.open('oreilly.jpg')
print(img.format)
print(img.size)
print(img.mode)
#img.show()

print('=' * 20)

crop = (265, 100, 450, 185)
img2 = img.crop(crop)
#img2.show()
img2.save('oreilly-cropped.gif', 'GIF')

img3 = Image.open('oreilly-cropped.gif')
print(img3.format)
print(img3.size)

print('=' * 20)

stache = Image.open('mustache.jpg').convert('RGBA')
stache.putalpha(200)
#stache.show()

###################################################################################################################
#                   Color change using for loop swap, processes in over 5 minutes on entire image
###################################################################################################################
# not in book, isolating black part of mustache and turning the background transparent
# modified from google ai example, suggests using numPy for much faster performace

stache.thumbnail((200, 100), resample=Image.Resampling.LANCZOS) # resize

def replace_color_on_image_and_transparent_everything_else(image_path, target_color, target_range, new_color):

    # check processing time
    start_time = time.time()
    print(f'%s\t Start time: %.4f' % (target_color, start_time))

    img = image_path

    data = img.getdata()
    new_data = []

    for item in data:

        # find colors within range of target_color (i.e: target 100 and range 50, replace between 75 and 125)
        #   true: replace with new color
        #   else: keep original color
        if item[0] >= target_color[0]-(target_range/2) and item[0] <= target_color[0]+(target_range/2) and\
                item[1] >= target_color[1]-(target_range/2) and item[1] <= target_color[1]+(target_range/2) and\
                item[2] >= target_color[1]-(target_range/2) and item[1] <= target_color[1]+(target_range/2):

            new_data.append(new_color)

            img.putdata(new_data)
        else :
            new_data.append((255, 255, 255, 0))

    img.putdata(new_data)
    #img.save(output_path, 'PNG')   # option to save image

    end_time = time.time()
    print(f'%s\t End time: %.4f' % (target_color, end_time))
    print(f'%s\t Elapsed time: %.4f' % (target_color, (end_time - start_time)))

    return img

stache = replace_color_on_image_and_transparent_everything_else(stache, (0,0,0), 100, (200,100,0,240))

img4 = Image.new('RGBA', img.size, (255, 255, 255, 0))
img4.paste(img, (0, 0))
img4.paste(stache, (280, 160), mask=stache)
#img4.show()

#result.save('oreilly-mustache.png', 'PNG')

print('=' * 20)

###################################################################################################################
#                   Color change using NumPy, processes in less than 10ms on entire image
###################################################################################################################
# google AI suggestion for fast numpy color swap

import numpy as np

def replace_color_with_transparent_fast(image_path, target_color, target_range, new_color):
    start_time = time.time()
    print(f'%s\t Start time: %.4f' % (target_color, start_time))

    if isinstance(image_path, str):
        img = Image.open(image_path).convert("RGBA")
    else :
        img = image_path

    data = np.array(img)
    r,g,b,a = data.T
    target_areas = (r >= target_color[0]-(target_range/2)) & (r <= target_color[0]+(target_range/2)) & \
                (g >= target_color[1]-(target_range/2)) & (g <= target_color[1]+(target_range/2)) & \
                (b >= target_color[2]-(target_range/2)) & (b <= target_color[2]+(target_range/2))

    data[target_areas.T] = new_color

    end_time = time.time()
    print(f'%s\t End time: %.4f' % (target_color, end_time))
    print(f'%s\t Elapsed time: %.4f' % (target_color, (end_time - start_time)))

    return Image.fromarray(data)

#img5 = Image.open("oreilly.jpg").convert("RGBA")

img5 = img4

# change a red to a purple color
img5 = replace_color_with_transparent_fast(img5, (200,0,0), 150, (100, 0, 100, 255))
# change a black to a yellow color
img5 = replace_color_with_transparent_fast(img5, (0,0,0), 150, (200, 200, 0, 255))
# change a white to a red color
img5 = replace_color_with_transparent_fast(img5, (255,255,255), 100, (200, 0, 0, 255))
# change an orange to black
img5 = replace_color_with_transparent_fast(img5, (200,100,0), 100, (0, 0, 0, 255))

img5.show()

#img5.save("new_image.png", "PNG")
