def solution(s: str):
    table = {'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}

    for i in table:
        if s.find(i) == -1:
            continue
        s = s.replace(i, str(table[i]))

    answer = int(s)
    return answer

print(solution(input()))