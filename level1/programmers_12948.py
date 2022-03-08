# 핸드폰 번호 가리기
def solution(phone_number):
    star = ['*'] * len(phone_number)
    for i in range(-4, 0):
        star[i] = phone_number[i]
    
    answer = ''
    for i in star:
        answer += ''.join(i)

    return answer

print(solution("01033334444"))