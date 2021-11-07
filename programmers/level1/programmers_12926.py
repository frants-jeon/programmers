def solution(s, n):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    num = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26]
    num_alphabet = {}
    alphabet_num = {}
    for i in range(26):
        num_alphabet[num[i]] = alphabet[i]
        alphabet_num[alphabet[i]] = num[i]

    upper_index = []
    for i in range(len(s)):
        if s[i].isupper():
            upper_index.append(i)
    s = s.lower()

    answer = ''
    for i in s:
        if i == ' ':
            answer += ' '
            continue
        if alphabet_num[i] + n > 26:
            answer += num_alphabet[n - (26 - alphabet_num[i])]
        else:
            answer += num_alphabet[alphabet_num[i] + n]
    answer_list = list(answer)
    for i in upper_index:
        answer_list[i] = answer_list[i].upper()

    answer = ''
    for i in range(len(answer_list)):
        answer += ''.join(answer_list[i])
    return answer

print(solution("a B z", 4))