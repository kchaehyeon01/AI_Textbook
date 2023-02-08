def AND(x1,x2):
    w1, w2, theta = 0.5, 0.5, 0.7 # 함수 안에서 초기화
    tmp = w1 * x1 + w2 * x2       # 가중치를 곱한 입력의 총합
    if tmp <= theta:              
        return 0                  # 임계값을 넘지 않으면 0을 반환
    elif tmp > theta:
        return 1                  # 임계값을 넘으면 1을 반환

print("\nAND(0,0) : 0을 출력?")
print(AND(0,0)) # 0을 출력

print("\nAND(1,0) : 0을 출력?")
print(AND(1,0)) # 0을 출력

print("\nAND(0,1) : 0을 출력?")
print(AND(0,1)) # 0을 출력

print("\nAND(1,1) : 1을 출력?")
print(AND(1,1)) # 1을 출력