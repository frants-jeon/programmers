# 하샤드 수
def solution(x):
    l = list(str(x))
    answer = 0
    for i in l:
        answer += int(i)
    if x % answer == 0:
        return True
    return False

print(solution(11))