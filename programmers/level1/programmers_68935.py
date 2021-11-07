def solution(n):
    total = 0
    while 1:
        t = 0 
        if n > 2:
            while 1:
                t += 1
                if 3 ** t <= n < 3 ** (t + 1): break
            total += 10 ** t
            n -= 3 ** t
        else:
            total += n
            break
    
    total = list(str(total))
    rev_total = []
    for _ in range(len(total)):
        rev_total.append(total.pop())

    answer = ''
    for i in rev_total:
        answer += ''.join(i)

    final_answer = 0
    for i in range(len(answer)):
        final_answer += int(answer[i]) * 3 ** (len(answer) - 1 - i)
    

    return final_answer

print(solution(45))