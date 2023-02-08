import numpy as np
import matplotlib.pyplot as plt

def step_function1(x): # 인수 x는 실수(부동소수점)만 받아들임 -> 넘파이 배열을 인수로 넣을 수 없음!
    if x > 0: return 1
    else: return 0

def step_function2(x): # NumPy 배열도 인수로 넣을 수 있도록 수정
    result = x > 0 # NumPy trick : NumPy 배열에 부등호 연산 수행 -> 배열 각 원소에 부등호 연산 수행한 bool 배열 생성
    return result.astype(np.int) # astype(원하는_자료형) 메서드 : NumPy 배열의 자료형 변환

def step_function3(x):
    return np.array(x>0, dtype=np.int)

# graph of step function
x = np.arange(-5.0,5.0,0.1) # -5.0에서 5.0 전까지 0.1 간격의 넘파이 배열 생성
y = step_function3(x) # 인수로 받은 넘파이 배열의 원소 각각을 인수로 계단 함수 실행 -> 결과를 다시 배열로 돌려줌
plt.plot(x,y)
plt.ylim(-0.1,1.1) # y축의 범위 지정
plt.show()