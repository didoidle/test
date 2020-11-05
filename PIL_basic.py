from PIL import Image
from scipy.ndimage import measurements,morphology
from numpy import *

# load image and threshold to make sure it is binary
pil_im = Image.open('IMG_0089.png').convert('L')
pil_im.save('color.jpg')
# make thumbnails
im = Image.open('IMG_0089.png')
im.thumbnail((128, 128))
im.save('thumbnail.jpg')

# copy and paste regions
im = Image.open('IMG_0089.png')
box = (100, 100, 400, 400)
box2 = (200, 500, 500, 800)
region = im.crop(box)
region = region.transpose(Image.ROTATE_180)
im.paste(region, box2)
im.save('paste.jpg')

# resize and rotate

im = im.resize((128, 128))
im = im.rotate(45)
im.save('resizeRotate.jpg')

labels, nbr_objects = measurements.label(pil_im)
print("Number of objects:", nbr_objects)

# morphology - opening to separate objects better
im_open = morphology.binary_opening(pil_im, ones((9, 5)), iterations=2)

labels_open, nbr_objects_open = measurements.label(im_open)
print("Number of objects:", nbr_objects_open)
Image.open('IMG_0089.png').save('abc.jpg')