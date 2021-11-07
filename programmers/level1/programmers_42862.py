def solution(n, lost, reserve):
    lost_list = []
    reserve_list = []

    for i in range(1, n + 1):
        lost_list.append(i)
        reserve_list.append(i)
    
    for i in range(n):
        # 체육복 분실했으면 0
        if lost_list[i] in lost:
            lost_list[i] = 0
        # 여벌 체육복 없으면 0
        if reserve_list[i] not in reserve:
            reserve_list[i] = 0

    for i in range(n):
        if lost_list[i] == 0 and reserve_list[i] > 0:
            lost_list[i] = i + 1
            reserve_list[i] = 0

    for i in range(n):
        if i == 0 and lost_list[i] == 0:
            if reserve_list[i + 1] != 0:
                lost_list[i] = i + 1
                reserve_list[i + 1] = 0

        elif i == n - 1 and lost_list[i] == 0:
            if reserve_list[i - 1] != 0:
                lost_list[i] = i + 1
                reserve_list[i - 1] = 0


        elif lost_list[i] == 0:
            if reserve_list[i - 1] != 0:
                lost_list[i] = i + 1
                reserve_list[i - 1] = 0

            elif reserve_list[i + 1] != 0:
                lost_list[i] = i + 1
                reserve_list[i + 1] = 0

    for i in range(lost_list.count(0)):
        lost_list.remove(0)
    

    answer = len(lost_list)
    return answer


n = 10
lost = [5,4,3,2,1]
reserve = [3,1,2,5,4]

print(solution(n, lost, reserve))