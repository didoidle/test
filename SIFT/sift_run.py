import sift
from numpy import *
from PIL import Image
from pylab import *

imname = 'IMG_0089.png'
im1 = array(Image.open(imname).convert('L'))
sift.process_image(imname,'IMG_0089.sift')
l1, d1 = sift.read_features_from_file('IMG_0089.sift')
figure()
gray()
sift.plot_features(im1, l1, circle=True)
show()