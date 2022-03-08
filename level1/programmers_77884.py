def solution(left, right):
    plus = []
    minus = []
    for i in range(left, right + 1):
        if i == 1:
            minus.append(i)
            continue
        diviser = 0
        for j in range(1, i + 1):
            if j > i // 2:
                diviser += 1
                break
            if i % j == 0:
                diviser += 1
        
        if diviser % 2 == 0:
            plus.append(i)
        else:
            minus.append(i)

    answer = 0
    for i in plus:
        answer += i

    for i in minus:
        answer -= i

    return answer


print(solution(24, 27))