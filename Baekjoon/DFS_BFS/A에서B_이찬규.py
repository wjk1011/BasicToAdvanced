# 정답

from collections import deque

A, B = list(map(int, input().split(' ')))
q = deque([[A, 0]])
answer = -2
while q:
    now = q.popleft()
    if now[0] * 2 < B:
        q.append([now[0] * 2, now[1]+1])
    elif now[0] * 2 == B:
        answer = now[1] + 1
        break
    if int(str(now[0]) + '1') < B:
        q.append([int(str(now[0]) + '1'), now[1] + 1])
    elif int(str(now[0]) + '1') == B:
        answer = now[1] + 1
        break
print(answer+1)
