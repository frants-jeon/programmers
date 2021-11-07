def solution(numbers:list):
    answer = {-1}
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            answer.add(numbers[i] + numbers[j])
    
    answer.remove(-1)
    answer = sorted(list(answer))
    return answer

test1 = [5,0,2,7]

print(solution(test1))