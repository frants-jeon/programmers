def solution(nums):
    prime_check = []
    for i in range(len(nums) - 2):
        for j in range(i + 1, len(nums) - 1):
            for k in range(j + 1, len(nums)):
                is_prime = nums[i] + nums[j] + nums[k]
                square_root = int(is_prime ** 0.5)
                for x in range(2, square_root + 1):
                    if is_prime % x == 0:
                        is_prime = False
                        break
                if is_prime:
                    prime_check.append(is_prime)

    answer = len(prime_check)
    return answer


a = [1,2,7,6,4]
print(solution(a))