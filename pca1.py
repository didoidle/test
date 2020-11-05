import cv2
from PIL import Image
from numpy import *
from pylab import *
import os
import pca2

def iter_files(path):
    for root, dirs, files in os.walk(path):
        for file in files:
            ext = os.path.splitext(file)[1][1:].lower()
            if ext in ['jpg', 'jpeg', 'png', 'gif']:
                yield os.path.join(root, file)

def iter_imgs(files):
    for file in files:
        yield cv2.imread(file,cv2.IMREAD_GRAYSCALE).flatten()

path = r'C:\Users\feifu\PycharmProjects\untitled\pca\lfw-deepfunneled'
oneImgPath = r'C:\Users\feifu\PycharmProjects\untitled\pca\lfw-deepfunneled\Aaron_Eckhart'
files = iter_files(path)

imgs = iter_imgs(files)
im = stack(imgs)
#print im.shape
img1 = array(Image.open('Aaron_Eckhart_0001.jpg'))
m, n = img1.shape[0:2]
#print m, n
imnbr = len(im[:, 0])
#print imnbr
V, S, immean = pca2.pca(im.T)

figure()
gray()
subplot(2,4,1)
imshow(immean.reshape(m, n))
for i in range(7):
    subplot(2,4,i+2)
    imshow(V[i].reshape(m, n))

show()

