# 제일 작은 수 제거하기
def solution(arr: list):
    if len(arr) == 1:
        return [-1]
    arr.remove(min(arr))
    return arr

print(solution([4,3,2,1]))