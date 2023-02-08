import numpy as np

X = np.array([1,2])
W = np.array([[1,3,5],[2,4,6]])
Y = np.dot(X,W)

print("\nX :\n", X, X.shape)
print("\nW :\n", W, W.shape)
print("\nY = np.dot(X,W) :\n", Y, Y.shape)