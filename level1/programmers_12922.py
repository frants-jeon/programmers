def solution(n):
    watermelon = '수박' * (n // 2)
    if n % 2 != 0:
        watermelon += ''.join('수')
    return watermelon

print(solution(10))