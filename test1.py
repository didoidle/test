import cv2
import scipy
from sklearn.cluster import KMeans
from skimage import exposure
#from scipy import ndimage, signal
#from skimage.filters import gaussian
from skimage import feature
#from skimage.filters import roberts, sobel, scharr, prewitt
import numpy as np
from pylab import *
import os
import pca2



def iter_files(path):
    for root, dirs, files in os.walk(path):
        for file in files:
            ext = os.path.splitext(file)[1][1:].lower()
            if ext in ['jpg', 'jpeg', 'png', 'gif']:
                yield os.path.join(root, file)

def com_center(points):
    var1 = np.mean(points[:, 0])
    var2 = np.mean(points[:, 1])
    center = [var1, var2]
    return center

def median_filter(img, size = 3):
    return scipy.signal.medfilt(img, size).astype(np.uint8)

def contrast_stretching(img):
    # Contrast stretching
    #p2, p98 = np.percentile(img, (0, 20))
    return exposure.rescale_intensity(img, in_range=(0.05*255, 0.6*255))

def canny(img):
    return feature.canny(img, sigma=1.8)

def find_theta_sort(points, center):
    points[:, 0] += 1000
    vec1 = np.array([0, 1])
    points_var = np.rint(np.sqrt(points[:, 0] * points[:, 0] + points[:, 1] * points[:, 1]))

    costheta = np.empty([0, 1])
    for i in np.arange(6):
        costheta = np.vstack((costheta, (np.dot(points[i], vec1.T) / points_var[i])))

    points = np.hstack((points, costheta))
    points = points[points[:, 2].argsort()]
    points = points[:, 0:2]

    points[:, 0] -= 1000
    points = np.vstack((points, center))

    return points


def iter_imgs(files):

        for file in files:

            a = np.array(cv2.imread(file))
            i = a.shape[0]
            j = a.shape[1]
            b = []
            width_px = np.shape(a)[1]
            print(i, j)
            for y in range(i):
                for x in range(j):
                    if (a[y][x][0] > 50):
                        continue
                        #a[y][x][0] = 0
                        #a[y][x][1] = 0
                        #a[y][x][2] = 0
                    if a[y][x][2] < 255:
                        continue
                        #a[y][x][0] = 0
                        #a[y][x][1] = 0
                        #a[y][x][2] = 0
                    else:
                        b.append([x, y])
            model = KMeans(n_clusters=6, init="k-means++", n_init=7, max_iter=10, random_state=None).fit(b)
            c1, c2, c3, c4, c5, c6 = np.rint(model.cluster_centers_)
            points = np.array([c1, c2, c3, c4, c5, c6])
            n_points = points / width_px
        return n_points , width_px

        #center1 = rint(com_center(points))
        #points_n = rint(points[:] - center1)
        #points.astype(int)
        #points_n = find_theta_sort(points_n, center1)
        #ips = vstack((ips, points_n))
        #print(ips)
def findedge():
    b=[]
    gray_img_path = r'C:\Users\feifu\PycharmProjects\untitled\pca\test2\1.png'
    a = cv2.imread(gray_img_path, cv2.IMREAD_GRAYSCALE)
    median = median_filter(np.array(a))
    contrast = contrast_stretching(median)
    ext_img = canny(contrast)
    #imshow(ext_img, cmap=plt.cm.gray)
    #axis('off')
    #plt.show()
    i = ext_img.shape[0]
    j = ext_img.shape[1]
    for y in range(i):
        for x in range(j):
            if a[y][x] == 1 :
                b.append([x, y])
    b = np.array(b)/j
    return b

def findedgenew():
    b = []
    gray_img_path = r'C:\Users\feifu\PycharmProjects\untitled\pca\test2\1.png'
    img1 = cv2.imread(gray_img_path, cv2.IMREAD_GRAYSCALE)
    img2 = cv2.GaussianBlur(img1, (5, 5), 5)
    points1 = cv2.Canny(img2, 30, 40, 1, 3)
    img3 = np.zeros(shape(img1),dtype=bool)
    img3[points1 > 0] = [1]
    imshow(img3, cmap=plt.cm.gray)
    axis('off')
    plt.show()

    i = img3.shape[0]
    j = img3.shape[1]
    for y in range(i):
        for x in range(j):
            if img1[y][x] == 1:
                b.append([x, y])
    b = np.array(b) / j
    return b

def comatrix(p_points, edges):
    mtx = np.empty([0,2])
    for i in range(shape(p_points)[0]):
        mtx = np.vstack((mtx, p_points[i]))
        e = np.empty([0, 1])
        for j in range(shape(edges)[0]):
            e = np.vstack((e, np.array([(edges[j][0]-p_points[i][0])**2 + (edges[j][1]-p_points[i][1])**2])))
        v = np.hstack((edges, e))
        v = v[v[:,2].argsort()]
        v = v[:,0:2]
        v = v[1:50,:]
        mtx = np.vstack((mtx, v))
    return mtx

path = r'C:\Users\feifu\PycharmProjects\untitled\pca\test'
ips = np.empty([0, 2])
files = iter_files(path)

p_points, width = iter_imgs(files)




edges = findedgenew()
mtx = comatrix(p_points, edges)
#print(mtx)
mtx = dot(mtx,mtx.T)
print(shape(mtx))
u, s, vt = linalg.svd(mtx)


