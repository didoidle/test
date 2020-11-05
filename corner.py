from pylab import *
from numpy import *
from PIL import Image
from scipy.ndimage import filters
import cornerD

im = array(Image.open('f1.jpg').convert('L'))
harrisim = cornerD.compute_harris_response(im)
filtered_coords = cornerD.get_harris_points(harrisim,6)
cornerD.plot_harris_points(im, filtered_coords)