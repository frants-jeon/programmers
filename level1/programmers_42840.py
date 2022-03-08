def solution(answers):
    score = [0,0,0]
    answer = []
    first_answer = [1,2,3,4,5]
    second_answer = [2,1,2,3,2,4,2,5]
    third_answer = [3,3,1,1,2,2,4,4,5,5]
    for one in range(len(answers)):
        if answers[one] == first_answer[one % 5]:
            score[0] += 1

    for two in range(len(answers)):
        if answers[two] == second_answer[two % 8]:
            score[1] += 1

    for three in range(len(answers)):
        if answers[three] == third_answer[three % 10]:
            score[2] += 1

    max_v = max(score)
    for i in range(3):
        if score[i] == max_v:
            answer.append(i + 1)
    
    return answer


answers = [1,1]

print(solution(answers))