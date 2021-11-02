import copy

def solution(participant: list, completion):
    answer = []
    for i in participant:
        if participant.count(i) != completion.count(i) + answer.count(i):
            answer.append(i)
    return answer

participant = ["mislav", "stanko", "mislav", "ana"]	
completion = ["stanko", "ana", "mislav"]	

print(solution(participant, completion))