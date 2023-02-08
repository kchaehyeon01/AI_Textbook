import numpy as np
x = np.array([0,1])     # 입력
w = np.array([0.5,0.5]) # 가중치
b = -0.7                # bias

print(np.sum(w*x)+b) # -0.19999999999999996 (부동소수점 수에 의한 연산 오차)