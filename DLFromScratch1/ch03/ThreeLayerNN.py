import numpy as np

def sigmoid(x):
    return 1/(1+np.exp(-x))

def identity_function(x):
    return x
    
def init_network(): # 가중치 & 편향을 초기화 -> 딕셔너리 변수 network에 저장
    network = {} # 각 층에 필요한 매개변수를 저장
    network['W1'] = np.array([[1.0,1.0,1.0],[1.0,1.0,1.0]]) # (2,3))
    network['b1'] = np.array([1.0,1.0,1.0]) # (3,)
    network['W2'] = np.array([[1.0,1.0],[1.0,1.0],[1.0,1.0]]) # (3,2)
    network['b2'] = np.array([1.0,1.0]) # (2,)
    network['W3'] = np.array([[1.0,1.0],[1.0,1.0]]) # (2,2)
    network['b3'] = np.array([1.0,1.0]) # (2,)

    return network

def forward(network,x): # 입력 신호를 출력으로 변환하는 처리 과정을 모두 구현 (신호가 순방향으로 전달됨 : 입력 -> 출력)
    W1, W2, W3 = network['W1'], network['W2'], network['W3']
    b1, b2, b3 = network['b1'], network['b2'], network['b3']

    a1 = np.dot(x,W1) + b1
    z1 = sigmoid(a1)
    a2 = np.dot(z1,W2) + b2
    z2 = sigmoid(a2)
    a3 = np.dot(z2,W3) + b3
    y = identity_function(a3)

    return y

network = init_network()
x = np.array([1.0,3.0])
y = forward(network,x)
print(y)