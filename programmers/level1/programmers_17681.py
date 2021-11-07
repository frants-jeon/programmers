def solution(n, arr1, arr2):
    binary_arr1 = []
    binary_arr2 = []

    for i in arr1:
        support = ''
        for j in range(n - 1, -1, -1):
            if i - 2 ** j >= 0:
                support += ''.join('1')
                i = i - 2 ** j
            else:
                support += ''.join('0')
        binary_arr1.append(support)
    
    for i in arr2:
        support = ''
        for j in range(n - 1, -1, -1):
            if i - 2 ** j >= 0:
                support += ''.join('1')
                i = i - 2 ** j
            else:
                support += ''.join('0')
        binary_arr2.append(support)
    
    answer = []
    for i in range(n):
        support = ''
        for j in range(n):
            if binary_arr1[i][j] == '0' and binary_arr2[i][j] == '0':
                support += ''.join(' ')
            elif binary_arr1[i][j] == '1' or binary_arr2[i][j] == '1':
                support += ''.join('#')
        answer.append(support)

    return answer


test1 = [9, 20, 28, 18, 11]
test2 = [30, 1, 21, 17, 28]
print(solution(len(test1), test1, test2))