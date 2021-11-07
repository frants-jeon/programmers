def solution(price, money, count):
    payment = 0
    for i in range(1, count + 1):
        payment += price * i
    
    if payment - money > 0:
        return payment - money
    else:
        return 0

print(solution(3,20,4))