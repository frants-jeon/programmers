# 정수 제곱근 판별
def solution(n):
    is_square_root = int(n ** 0.5)
    if is_square_root ** 2 == n:
        answer = (is_square_root + 1) ** 2
    else:
        answer = -1
    return answer

print(solution(3))