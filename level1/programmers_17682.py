def solution(dartResult: str):
    answer = []
    square = 'xSDT'
    for i in range(len(dartResult)):
        pointer = dartResult[i]
        if pointer in square:
            if dartResult[i - 2] == '1' and dartResult[i - 1] == '0':
                answer.append(10 ** square.index(pointer))
            else:
                answer.append(int(dartResult[i - 1]) ** square.index(pointer))
        elif pointer == '*':
            if len(answer) == 1:
                answer[-1] = answer[-1] * 2
            else:
                answer[-1] = answer[-1] * 2
                answer[-2] = answer[-2] * 2
        elif pointer == '#':
            answer[-1] = answer[-1] * -1


    return sum(answer)

print(solution("1D2S#10S"))