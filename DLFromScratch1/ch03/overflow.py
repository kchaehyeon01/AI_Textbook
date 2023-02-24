import numpy as np

a = np.array([1010,1000,990])
max = np.max(a)

overflow = np.exp(a)/np.sum(np.exp(a)) # sofrmax 함수의 계산
minusmax = np.exp(a-max)/np.sum(np.exp(a-max))

print("overflow:", overflow) 
print("\t\t--> this will be nan : not a number!")
print("minusmax:", minusmax)