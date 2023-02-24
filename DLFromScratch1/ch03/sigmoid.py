import numpy as np
import matplotlib.pyplot as plt

def sigmoid(x): # 인수 x가 NumPy 배열이어도 올바른 결과 나옴
    return 1/(1+np.exp(-x)) # broadcast

x = np.arange(-5.0,5.0,0.1)
y = sigmoid(x)
plt.plot(x,y)
plt.ylim(-0.1,1.1)
plt.show()