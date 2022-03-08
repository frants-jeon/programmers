def solution(s):
    answer = ''
    s = sorted(list(s), reverse=True)
    for i in range(len(s)):
        answer += ''.join(s[i])
    return answer

print(solution('Zbcdefg'))