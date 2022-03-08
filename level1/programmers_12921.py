def is_prime(n):
    if n == 1:
        return False

    i = 2
    while i*i <= n:
        if n % i == 0:
            return False
        i += 1
    return True
prime_number = []
for i in range(2, 1000000):
    if is_prime(i):
        prime_number.append(i)
def solution(n):
    global prime_number
    answer = len([x for x in prime_number if x <= n])

    return answer

print(solution(1000))