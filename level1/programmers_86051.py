def solution(numbers):
    all_num = [0,1,2,3,4,5,6,7,8,9]
    no_num = []
    for i in all_num:
        if i not in numbers:
            no_num.append(i)
    answer = sum(no_num)
    return answer


