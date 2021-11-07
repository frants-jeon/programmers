def solution(a, b):
    answer = 0
    if a > b:
        a, b = b, a
    
    # if a < 0:
    #     if abs(a) > abs(b):
    #         b = a + b
    #     elif abs(a) < abs(b):
    #         a = abs(a) + 1
    #     else:
    #         return 0

    for i in range(a, b + 1):
        answer += i

    return answer

print(solution(-3, 10))