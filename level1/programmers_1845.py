def solution(nums):
    cnt_type = set(nums)
    pick = len(nums) / 2

    if len(cnt_type) >= pick:
        answer = pick
    else:
        answer = len(cnt_type)
    return int(answer)


test = [3,1,2,3]
if __name__ == '__main__' :
    print(solution(test))