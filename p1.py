import cv2
import numpy as np
import matplotlib.pyplot as plt

trainData = np.random.randint(0, 100, (50, 2)).astype(np.float32)

responses = np.random.randint(0, 2, (50, 1)).astype(np.float32)

red = trainData[responses.ravel() == 0]
plt.scatter(red[:, 0], red[:, 1], 50, 'r', '^')

blue = trainData[responses.ravel() == 1]
plt.scatter(blue[:, 0], blue[:, 1], 50, 'b', 's')

newcomer = np.random.randint(0, 100, (3, 2)).astype(np.float32)
plt.scatter(newcomer[:, 0], newcomer[:, 1], 50, 'g', 'o')

knn = cv2.ml.KNearest_create()
knn.train(trainData, cv2.ml.ROW_SAMPLE, responses)
ret, results, neighbours, dist = knn.findNearest(newcomer, 15)

print("result: ", results, "\n")
print("neighbours: ", neighbours, "\n")
print("distance: ", dist)

plt.show()