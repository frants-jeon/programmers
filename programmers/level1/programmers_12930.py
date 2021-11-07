def solution(s):
    words = s.split(" ")
    upper_word = []
    for word in words:
        if word == '':
            upper_word.append(' ')
            continue
        word = list(word)
        box = ''
        for j in range(len(word)):
            if j % 2 == 0:
                word[j] = word[j].upper()
            else:
                word[j] = word[j].lower()
                
        box = ''.join(word)
        upper_word.append(box)
    print(upper_word)
    answer = ''
    for i in upper_word:
        answer += i
        if i != ' ':
            answer += ' '

    return answer[:-1]

print(solution("qqr   owu  qhBBr oiy  "))