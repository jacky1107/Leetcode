def solution(S):
    ans = 0
    while num > 0:
        if num % 2: num -= 1
        else: num /= 2
        ans += 1
    return ans

solution("011100")
solution("1111010101111")
s = '1' * 400000
solution(s)
