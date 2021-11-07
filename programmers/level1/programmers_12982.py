def solution(d, budget):
    if sum(d) <= budget:
        answer = len(d)
        return answer
    
    else:
        d.remove(max(d))
        solution(d, budget)
    
    return len(d)

test1 = [1,3,2,5,4]
test2 = 9
print(solution(test1, test2))