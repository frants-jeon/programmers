def solution(answers):
    reset = 0
    score = [0,0,0]
    first_answer = [1,2,3,4,5]
    second_answer = [2,1,2,3,2,4,2,5]
    third_answer = [3,3,1,1,2,2,4,4,5,5]
    for one in range(len(answers)):
        if one % 5 == 0 and one > 0:
            reset += 5
        if answers[one] == first_answer[one - reset]:
            score[0] += 1

    reset = 0
    for two in range(len(answers)):
        if two % 8 == 0 and two > 0:
            reset += 8
        if answers[two] == second_answer[two - reset]:
            score[1] += 1

    reset = 0
    for three in range(len(answers)):
        if three % 10 == 0 and three > 0:
            reset += 10
        if answers[three] == third_answer[three - reset]:
            score[2] += 1

    if len(set(score)) == 1:
        return [1,2,3]
    elif len(set(score)) == 2 and 0 not in set(score):
        score[score.index(min(score))] = 0
        for i in range(3):
            if score[i] != 0:
                score[i] = i + 1
        score.pop(score.index(min(score)))
        return score
    else:
        return [score.index(max(score)) + 1]

answers = [1,2,3,4,5,2] * 1500

print(solution(answers))