##### 오픈채팅방 #####
# https://programmers.co.kr/learn/courses/30/lessons/42888
def solution(record):
  answer = []
  actions = []
  id_dict = dict()
  for info in record:
    info = list(info.split())
    action, user_id = info[0], info[1]
    if len(info) > 2:
      nick_name = info[2]
      id_dict[user_id] = nick_name
    actions.append([action, user_id])
  
  for i in range(len(actions)):
    a = id_dict[actions[i][1]]
    if actions[i][0] == 'Enter':
      b = '들어왔'
    elif actions[i][0] == 'Leave':
      b = '나갔'
    else: continue
    answer.append(a + '님이 ' + b + '습니다.')
  return answer

test = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]
print(solution(test))