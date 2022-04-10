##### 더 맵게 #####
# https://programmers.co.kr/learn/courses/30/lessons/42626
from heapq import heappush, heappop, heapify
def solution(scoville, K):
  heapify(scoville)
  answer = 0
  while scoville:
    low = heappop(scoville)
    if low >= K: break
    # low < K 인 상황에서 섞을 음식이 남아있지 않다면 조건을 충족하지 못하므로 -1 리턴
    if not scoville:
      answer = -1
      break
    new = low + heappop(scoville) * 2
    heappush(scoville, new)
    answer += 1
  
  return answer

test1 = [1, 2, 3, 9, 10, 12]
test2 = 7
print(solution(test1, test2))