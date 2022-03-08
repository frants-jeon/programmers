def solution(N, stages):
    before_stage = 0
    failure_rate = []
    for i in range(1, N + 1):
        this_stage = stages.count(i)
        if len(stages) - before_stage == 0:
            failure_rate.append(0)
        else:
            failure_rate.append(this_stage / (len(stages) - before_stage))
        before_stage += this_stage
    
    answer = [-1]
    rev_sort_fr = [-1]
    for i in range(len(failure_rate)):
        for j in range(len(rev_sort_fr)):
            if failure_rate[i] > rev_sort_fr[j]:
                rev_sort_fr.insert(j, failure_rate[i])
                answer.insert(j, i + 1)
                break

    answer.remove(-1)
    
    return answer

test1 = 5
test2 = [2,2,2,2,2]
print(solution(test1, test2))