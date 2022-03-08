def solution(s):
    lenth = len(s)
    if lenth % 2 == 0:
        return s[lenth//2 - 1: lenth//2 + 1]
    else:
        return s[(lenth - 1) // 2]

print(solution('abcdef'))