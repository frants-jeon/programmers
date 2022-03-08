# 자연수 뒤집어 배열로 만들기
def solution(n):
    answer = list(str(n))
    for i in range(len(answer)):
        answer[i] = int(answer[i])
    answer.reverse()
    return answer

print(solution(12345))