def solution(s: str):
    s = s.lower()
    cnt_p = s.count('p')
    cnt_y = s.count('y')
    if cnt_p == cnt_y:
        return True
    else:
        return False

print(solution('PyYppy'))