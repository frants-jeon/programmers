def solution(absolutes, signs):
    signs_re = []
    integer = []
    for i in signs:
        if i:
            signs_re.append(1)
        else:
            signs_re.append(-1)
    
    for i in range(len(absolutes)):
        integer.append(absolutes[i] * signs_re[i])
    
    answer = sum(integer)
    return answer


a = [4,7,12]
b = [True,False,True]

print(solution(a,b))