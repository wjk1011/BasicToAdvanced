# 정답

from collections import deque

N, K = list(map(int, input().split(' ')))

q, visit = deque([N]), [-1] * 100001
visit[N] = 0
while q:
    x = q.popleft()
    if x == K:
        print(visit[x])
        break
    else:
        for dx in (x, -1, 1):
            if 0 <= x+dx <= 100000 and visit[x + dx] == -1:
                if dx == x:
                    visit[x+dx] = visit[x]
                    q.appendleft(x + dx)
                else:
                    visit[x + dx] = visit[x] + 1
                    q.append(x + dx)
