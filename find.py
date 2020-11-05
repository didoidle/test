import cv2
from numpy import *
from scipy.spatial import Delaunay

img1 = cv2.imread('f1.jpg')
img2 = cv2.imread('f1.jpg', cv2.IMREAD_GRAYSCALE)
img2 = cv2.GaussianBlur(img1, (3, 5), 5)
points1 = cv2.Canny(img2, 30, 40, 1, 3)

img1[points1 > 0] = [0, 0, 255]

cv2.imwrite('canny1.jpg', points1)

points2 = cv2.cornerHarris(points1, 2, 27, 0.24)

points2 = cv2.dilate(points2, None)

#if all(points2[i] < 0.2*points2.max() for i in points2):



img1[points2 > 0.03*points2.max()] = [0, 255, 0]


cv2.imshow('dst', img1)
if cv2.waitKey(0) & 0xff == 27:
    cv2.destroyAllWindows()
cv2.imwrite('canny2.jpg', img1)
