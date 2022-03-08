def solution(lottos, win_nums):
    correct = 0
    for i in win_nums:
        if i in lottos:
            correct += 1
    answer = []
    answer.append(correct)
    print(answer)
    return answer

solution([7,8,3,4,5,6],[6,5,4,3,2,1])