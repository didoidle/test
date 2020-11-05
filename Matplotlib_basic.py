from PIL import Image
from pylab import *

# read image to array
im = array(Image.open('IMG_0089.png'))
# plot the image
imshow(im)
# some points
x = [100,100,400,400]
y = [200,500,200,500]
# plot the points with red star-markers
plot(x,y,'r*')
# line plot connecting the first two points
plot(x[:2],y[:2])
# add title and show the plot
title('Plotting: "UBWD.jpg"')
# show()

im = array(Image.open('IMG_0089.png').convert('L'))

figure()
gray()
contour(im, origin='image') # only 2D
axis('equal')
axis('off')
figure()
# histogram
hist(im.flatten(), 128)
show()
