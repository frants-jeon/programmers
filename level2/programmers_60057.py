def solution(s):
    answer = []
    for div in range(1, len(s) // 2 + 1):
        l = []
        a = 0
        b = div
        for i in range(len(s) // div):
            if i == len(s) // div - 1:
                l.append(s[a:])
            else:
                l.append(s[a:b])
            if b < len(s):
                a += div
                b += div
        if len(s) % div > 0:
            l[-1] = l[-1] + s[b:]
        compress = []
        cnt = 1
        for i in range(len(l)):
            if i < len(l) - 1:
                if l[i] == l[i + 1]:
                    cnt += 1
                    if i == len(l) - 2:
                        compress.append(f'{cnt}{l[i]}')
                    continue
            if cnt == 1:
                compress.append(l[i])
            else:
                compress.append(f'{cnt}{l[i]}')
                cnt = 1
        if compress[-1] == compress[-2]:
            compress.pop()
        cnt_len = 0
        for i in compress:
            cnt_len += len(i)
        answer.append(cnt_len)
    
    if len(answer) == 0:
        return len(s)
    else:
        answer = min(answer)

    return answer

test = 'abcabcdede'
print(len(test))
print(solution(test))