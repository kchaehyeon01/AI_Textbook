import numpy as np

def OR(x1,x2):
    x = np.array([x1,x2])
    w = np.array([0.5,0.5])
    b = -0.3
    tmp = np.sum(w*x) + b
    if tmp <= 0:
        return 0
    else:
        return 1
    
# x1 = float(input("x1 : "))
# x2 = float(input("x2 : "))
# print(OR(x1,x2))