def solution(strings, n):
    answer = []
    alphabet_number = []
    n_alphabet = []
    dic_alphabet_number = []
    dic_alphabet = []
    for i in strings:
        alphabet_number.append(f'{i[n]}{strings.index(i)}')
        n_alphabet.append(i[n])
    
    for i in alphabet_number:
        if n_alphabet.count(i[0]) > 1:
            dic_alphabet.append(strings[int(i[1])])
            dic_alphabet_number.append(i)

    alphabet_number = sorted(alphabet_number)
    dic_alphabet = sorted(dic_alphabet)
    for i in alphabet_number:
        if i in dic_alphabet_number:
            for j in dic_alphabet:
                if j[n] == i[0]:
                    answer.append(j)
                    dic_alphabet.remove(j)
                    break
        else:
            answer.append(strings[int(i[1])])

    return answer

test1 = ["abce", "abcd", "cdx"]	
print(solution(test1, 2))