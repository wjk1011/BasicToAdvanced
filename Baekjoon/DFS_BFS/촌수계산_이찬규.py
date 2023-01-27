# 정답

from collections import deque

n = int(input())
ox, oy = list(map(int, input().split(' ')))
m = int(input())
arr = [list(map(int, input().split(' '))) for i in range(m)]

d_c, d_p = {i+1: [] for i in range(n)}, {i+1: [] for i in range(n)}
for x,y in arr:
    d_p[y].append(x)
    d_c[x].append(y)

q, visited = deque([[ox, 0]]), []
answer = -1
while q:
    now = q.popleft()
    visited.append(now[0])

    now_child = d_c[now[0]]
    now_parent = d_p[now[0]]
    if oy in now_child or oy in now_parent:
        answer = now[1]+1
        break
    for p in now_parent:
        if p not in list(map(lambda x: x[0], q)) and p not in visited:
            q.append([p, now[1] + 1])
    for c in now_child:
        if c not in list(map(lambda x: x[0], q)) and c not in visited:
            q.append([c, now[1] + 1])

print(answer)

