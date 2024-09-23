def solution(S):
    table = {}
    count = 1 
    for i in range(len(S)):
        if S[i] not in table:
            table[S[i]] = i
        else:
            table = {}
            table[S[i]] = i
            count += 1
    return count

print(solution("abacdec"))
print(solution("abba"))
print(solution("cycle"))
print(solution("dddd"))
