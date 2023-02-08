import numpy as np

# 1D array ###########################
print("1D array ====================")
A = np.array([1,2,3,4])
print("A :",A)

# 배열의 차원 수 : np.ndim() 함수로 확인
print("np.ndim(A) (배열의 차원 수) :",np.ndim(A))

# 배열의 형상 : 인스턴스 변수 shape으로 확인 (튜플 반환 : 다차원 배열일 때와 통일된 형태로 결과 반환하기 위함)
print("A.shape (배열의 형상) :",A.shape)
print("A.shape[0] :",A.shape[0])

print("\n")

# 2D array ###########################
print("2D array ====================")
B = np.array([[1,2],[3,4],[5,6]])
print("B :",B)
print("np.ndim(B) (배열의 차원 수) :",np.ndim(B))
print("B.shape (배열의 형상) :",B.shape)