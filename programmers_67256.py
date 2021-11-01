def solution(number, hand):
    array = [[1,2,3], [4,5,6], [7,8,9], ['*',0,'#']]

    # number = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]
    # hand = 'right'
    answer = []

    target_pos = (0, 0)
    left_pos = (3,0)
    right_pos = (3,2)
    pad = {1: 'L', 2: 'mid', 3: 'R', 4: 'L', 5: 'mid', 6: 'R', 7: 'L', 8: 'mid', 9: 'R', 0: 'mid'}

    for i in number:
        for x in range(4): # array length
            for y in range(3):
                if i == array[x][y]:
                    target_pos = (x, y)
                    continue

        if pad[i] != 'mid':
            answer.append(pad[i])
            if pad[i] == 'L':
                left_pos = target_pos
            else:
                right_pos = target_pos
        else:
            l_distance = abs(target_pos[0] - left_pos[0]) + abs(target_pos[1] - left_pos[1])
            r_distance = abs(target_pos[0] - right_pos[0]) + abs(target_pos[1] - right_pos[1])

            if r_distance < l_distance:
                answer.append('R')
                right_pos = target_pos
            elif l_distance < r_distance:
                answer.append('L')
                left_pos = target_pos
            elif hand == 'right':
                answer.append('R')
                right_pos = target_pos
            else: 
                answer.append('L')
                left_pos = target_pos
                
    answer_final = ''
    for i in answer:
        answer_final += ''.join(i)
    
    return answer_final

num = 	[7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2]
hand = 'left'
print(solution(num, hand))

# 1시간 30분 소요ㅠㅠ