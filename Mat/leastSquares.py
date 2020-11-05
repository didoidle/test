from numpy import *

m = random.randint(0, 15, (3, 3))
print(m)

obj = random.randint(5, 50, (2, 10))
print(obj)

Mat = ([sum(obj[0, :]*obj[0, :]), sum(obj[0, :]*obj[1, :]), sum(obj[0, :])],
       [sum(obj[0, :]*obj[1, :]), sum(obj[1, :]*obj[1, :]), sum(obj[1, :])],
       [sum(obj[0, :]), sum(obj[1, :]), 10])
print(Mat)
Mat2 = ([sum(obj[0, :]*obj[0, :]*obj[0, :])+sum(obj[1, :]*obj[1, :]*obj[0, :])],
        [sum(obj[0, :]*obj[0, :]*obj[1, :])+sum(obj[1, :]*obj[1, :]*obj[1, :])],
        [sum(obj[0, :]**2)+sum(obj[1, :]**2)])
print(Mat2)
Mat3 = linalg.solve(Mat, Mat2)
print(Mat3)

print("(x - " , Mat3[0]/2 , ")^2 + (y - " , Mat3[1]/2 , ")^2 = " , Mat3[2] + (Mat3[0]/2) ** 2 + (Mat3[1]/2) ** 2)