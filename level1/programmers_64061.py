def solution(board, moves):
    basket = []
    answer = 0
    for crane in moves:
        crane -= 1
        for line in board:
            if line[crane] != 0:
                basket.append(line[crane])
                line[crane] = 0
                if len(basket) > 1:
                    if basket[-1] == basket[-2]:
                        basket.remove(basket[-1])
                        basket.remove(basket[-1])
                        answer += 2
                break
    
    # while 1:
    #     check = 0
    #     for i in range(1, len(basket)):
    #         if basket[i - 1] == basket[i]:
    #             answer += 2
    #             basket.pop(i - 1)
    #             basket.pop(i - 1)
    #             break
    #         else:
    #             check += 1
    #     if check == len(basket) - 1 or len(basket) == 0: break


    return answer



# board = [[0,0,0,0,1],[0,0,0,0,2],[0,0,0,0,3],[0,0,0,0,0],[0,0,0,0,0]]
# board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]	
# moves = [1,5,3,5,1,2,1,4]
board = [[0, 0, 1, 0, 0], [0, 0, 1, 0, 0], [0, 2, 1, 0, 0], [0, 2, 1, 0, 0], [0, 2, 1, 0, 0]]
moves = [1, 2, 3, 3, 2, 3, 1]
print(solution(board, moves))