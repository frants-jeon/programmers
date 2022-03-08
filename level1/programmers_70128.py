def solution(a, b):
    dot_product = []
    for i in range(len(a)):
        dot_product.append(a[i] * b[i])
    answer = sum(dot_product)
    return answer


a = [1,2,3,4]
b = [-3, -1, 0, 2]

print(solution(a,b))