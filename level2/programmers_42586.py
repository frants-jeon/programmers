##### 기능개발 #####
# https://programmers.co.kr/learn/courses/30/lessons/42586
from collections import deque

def solution(progresses, speeds):
  progresses = deque(progresses)
  speeds = deque(speeds)
  answer = []
  while progresses:
    # 각 작업마다 개발속도만큼 작업률 더해주고
    for i in range(len(progresses)):
      progresses[i] += speeds[i]

    cnt = 0 # 한 번에 배포한 작업 수
    while 1:
      # 제일 앞의 기능이 개발 완료되었으면 배포 가능한 것들 모두 배포(popleft)
      if progresses and progresses[0] >= 100:
        progresses.popleft()
        speeds.popleft()
        cnt += 1 # 배포한 작업 수 += 1
      else: break
    if cnt != 0: # 배포한 작업이 있다면 answer에 추가
      answer.append(cnt)

  return answer

test1 = [95, 90, 99, 99, 80, 99]
test2 = [1,1,1,1,1,1]
print(solution(test1, test2))