def solution(arr, divisor):
    answer = []
    for i in arr:
        if i % divisor == 0:
            answer.append(i)
    if len(answer) == 0:
        return [-1]
    else:
        return sorted(answer)


print(solution([2, 36, 1, 3], 1))