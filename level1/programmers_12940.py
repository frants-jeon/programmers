# 최대공약수와 최소공배수
def solution(n, m):
    if n > m:
        n, m = m, n
    m_diviser = []
    n_diviser = []
    answer = []
    for i in range(1, m // 2 + 1):
        if m % i == 0:
            m_diviser.append(i)
    m_diviser.append(m)
    
    for i in range(1, n // 2 + 1):
        if n % i == 0:
            n_diviser.append(i)
    n_diviser.append(n)
        
    for i in range(len(n_diviser) - 1, -1, -1):
        if n_diviser[i] in m_diviser:
            answer.append(n_diviser[i])
            break
    
    m_multiple = m
    n_multiple = n
    while m_multiple != n_multiple:
        if m_multiple < n_multiple:
            m_multiple += m
        elif m_multiple > n_multiple:
            n_multiple += n
    answer.append(n_multiple)

    return answer

print(solution(2,5))