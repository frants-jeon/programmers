##### 신고 결과 받기 #####

def solution(id_list, report, k):
    answer = [0] * len(id_list)
    # key = 신고 당한사람 / value = 신고한사람 형태의 dict 할당
    reported = {name: set() for name in id_list}
    # 특정 id가 answer의 몇 번째 idx인지 저장할 dict
    id_idx = {id_list[i]: i for i in range(len(id_list))}

    # 신고 내용 reported에 저장
    for rep in report:
      a, b = rep.split() # a는 신고당한 id, b는 신고한 id
      reported[b].add(a)

    for val in reported.values(): # 신고당한 사람들 목록을 돌면서
      if len(val) >= k: # 한 아이디에 신고건이 k건 이상이면
        for name in val: # 신고한 사람들 idx찾아서 +1 해줌
          answer[id_idx[name]] += 1
    return answer


test1 = ['muzi', 'frodo', 'apeach', 'neo']
test2 = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
print(solution(test1, test2, 2))