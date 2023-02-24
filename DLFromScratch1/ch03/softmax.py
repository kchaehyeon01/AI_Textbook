import numpy as np

def softmax(a):
    exp_a = np.exp(a)
    sum_exp_a = np.sum(exp_a)
    return exp_a/sum_exp_a

def softmax(a): # overflow 문제 해결하도록 함수 구현 개선
    max = np.max(a)
    exp_a = np.exp(a-max) # overflow 대책
    sum_exp_a = np.sum(exp_a)
    return exp_a/sum_exp_a