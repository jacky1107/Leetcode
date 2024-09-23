def solution(N):
    # write your code in Python 3.6
    B = N % 9 # 7
    A = N // 9 # 0
    print(A, B)
    res = str(B) + A * '9'
    return int(res)

r = solution(19)
print(r)
