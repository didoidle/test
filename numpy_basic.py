import numpy as np
from PIL import Image
im = np.array(Image.open('IMG_0089.png'))
print(im.shape, im.dtype)

im = np.array((Image.open('IMG_0089.png')).convert('L'), 'f')
print im.shape, im.dtype

i = np.array([[1,2,3],
     [4,5,6],
     [7,8,9]])
print i[0,:]
print i[:,0]
print (i[:2, :1].sum())

print int(im.min()), int(im.max())

# Graylevel transforms

im = np.array((Image.open('IMG_0089.png')).convert('L'))

# invert image
im2 = 255 - im

