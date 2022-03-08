# 정수 내림차순으로 배치하기
def solution(n):
    l = sorted(list(str(n)), reverse=True)
    answer = ''
    for i in l:
        answer += ''.join(i)
    answer = int(answer)
    return answer

print(solution(118372))