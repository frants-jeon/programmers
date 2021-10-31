def solution(new_id):
    x = '~!@#$%^&*()=+[{]}:?,<>/'
    # level1 소문자 치환
    level1 = list(new_id.lower()) 

    # level2 특수문자 제거
    level2 = []
    for i in level1:
        if i  not in x:
            level2.append(i)
    
    # level3 연속된 . 제거
    level3 = [level2[0]]
    for i in range(1, len(level2)):
        if level3[-1] == '.' and level2[i] == '.':
            continue
        level3.append(level2[i])
    # level4 처음과 끝의 . 제거
    level4 = []
    for i in range(len(level3)):
        if i == 0 and level3[i] == '.':
            continue
        if i == level3[-1] and level3[i] == '.':
            continue
        level4.append(level3[i])


    # # level5 빈문자면 a대입
    # if len(answer) == 0:
    #     for i in range(3):
    #         answer.append('a')
    
    # #level6 문자열 15개로 맞추기
    # r = []
    # if len(answer) > 15:
    #     for i in range(15, len(answer)):
    #         answer[i] = '?'
    #         r.append('?')
    #     for i in r:
    #         answer.remove(i)
    #     if answer[14] == '.':
    #         answer.remove(answer[14])
            
    # # level7 문자수 최소 3개 맞추기
    # while len(answer) < 3:
    #     last = answer[len(answer) - 1]
    #     answer.append(last)

    # answer_final = ''
    # for i in answer:
    #     answer_final += ''.join(i)
    # answer = answer_final

    
    return level4


print(solution(input()))
    