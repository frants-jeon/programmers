def solution(participant: list, completion):
    answer = list(set(participant) - set(completion))
    if len(answer) == 1:
        return answer[0]
    participant = sorted(participant)
    completion = sorted(completion)
    for i in range(len(completion)):
        if participant[i] != completion[i]:
            answer.append(participant[i])
            break

    return answer[0]

participant = ["mislav", "stanko", "mislav", "ana"]	
completion = ["stanko", "ana", "mislav"]	

print(solution(participant, completion))