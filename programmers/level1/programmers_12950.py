# 행렬의 덧샘
def solution(arr1, arr2):
    height = len(arr1[0])
    width = len(arr1)
    answer = []
    for i in range(width):
        answer.append([])
        for j in range(height):
            plus = arr1[i][j] + arr2[i][j]
            answer[i].append(plus)
    return answer

test1 = [[1,2],[2,3]]
test2 = [[3,4],[5,6]]
# print(test1[0][1])
print(solution(test1, test2))