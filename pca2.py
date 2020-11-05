
from numpy import *

def pca(X):
    num_data, dim = X.shape
    print(X.shape, "aaa")
    mean_X = X.mean(axis=0)
    X = X - mean_X
    if dim>num_data:
        X = dot(X,X.T)
    if dim<num_data:
        M = dot(X, X.T)
      #  print M.shape, "sss"
        e, EV = linalg.eigh(M)
        tmp = dot(X.T, EV).T
        V = tmp[::-1]
        S = sqrt(e)[::-1]
        #print S
        #S

        for i in range(V.shape[1]):
            V[:, i] /= S
    #else:
    U, S, V = linalg.svd(X)
    V = V[:num_data]
    return V, S, mean_X