import numpy as np
import matplotlib.pyplot as plt

def sigmoid(x):
    return 1/ (1+np.exp(-x)) 
def step_function3(x):
    return np.array(x>0, dtype=np.int)

x = np.arange(-5.0,5.0,0.1)
y1 = step_function3(x)
y2 = sigmoid(x)

plt.plot(x,y1,label="step function")
plt.plot(x,y2,label="sigmoid function")
plt.title("Step Function VS Sigmoid Function")
plt.ylim(-0.1,1.1)
plt.legend()
plt.show()