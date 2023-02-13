# 정답

from collections import deque


N, M = list(map(int, input().split(' ')))
d_ls = {}
for _ in range(N):
    i, j = list(map(int, input().split(' ')))
    d_ls[i] = j
for _ in range(M):
    i, j = list(map(int, input().split(' ')))
    d_ls[i] = j

q, visited = deque([[1, 0]]), []
while q:
    loc, time = q.popleft()
    visited.append(loc)
    for i in range(1,7):
        next = loc + i
        if next not in visited:
            if next in d_ls:
                next = d_ls[next]

            q.append([next,time+1])
            visited.append(next)
    if loc == 100:
        print(time)
        break
