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

stache = replace_color_on_image_and_transparent_everything_else(stache, (0,0,0), 100, (0,0,0,240))

img4 = Image.new('RGBA', img.size, (255, 255, 255, 0))
img4.paste(img, (0, 0))
img4.paste(stache, (280, 160), mask=stache)
#img4.show()

#result.save('oreilly-mustache.png', 'PNG')

print('=' * 20)

# google AI suggestion for fast numpy color swap
# needs work

import numpy as np

def replace_color_with_transparent_fast(image_path, target_color, output_path):
    start_time = time.time()
    print(f'%s\t Start time: %.4f' % (target_color, start_time))

    img = Image.open(image_path).convert("RGBA")
    data = np.array(img)
    r,g,b,a = data.T
    target_areas = (r == target_color[0]) & (g == target_color[1]) & (b == target_color[2])
    data[..., 3][target_areas.T] = 0

    new_img = Image.fromarray(data)
    new_img.save(output_path, "PNG")

    end_time = time.time()
    print(f'%s\t End time: %.4f' % (target_color, end_time))
    print(f'%s\t Elapsed time: %.4f' % (target_color, (end_time - start_time)))

replace_color_with_transparent_fast('oreilly.jpg', (0,0,0), "numpy-fast-color-change.png")
