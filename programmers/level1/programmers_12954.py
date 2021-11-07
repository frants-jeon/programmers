# x만큼 간격이 있는 n개의 숫자
def solution(x, n):
    answer = [x]
    while len(answer) < n:
        answer.append(answer[-1] + x)
    return answer

print(solution(-4,2))