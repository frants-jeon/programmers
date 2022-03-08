def solution(a, b):
    day7 = {0: 'FRI', 1: 'SAT', 2: 'SUN', 3: 'MON', 4: 'TUE', 5: 'WED', 6: 'THU'}
    month12 = {1: 31, 2: 29, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
    day360 = 0
    if a > 1:
        for i in range(1, a):
            day360 += month12[i]
    
    day360 += b - 1
    
    day = day7[(day360) % 7]

    return day


print(solution(3,15))