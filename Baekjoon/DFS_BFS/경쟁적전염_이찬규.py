# 정답

from collections import deque
from copy import deepcopy


N, K = list(map(int, input().split(' ')))
arr = [list(map(int, input().split(' '))) for _ in range(N)]
S, X, Y = list(map(int, input().split(' ')))

d_virus = {i+1: [] for i in range(K)}
q = deque()
for i, c in enumerate(arr):
    for j, v in enumerate(c):
        if v != 0:
            d_virus[v].append((i, j))

for i in d_virus:
    q.extend(d_virus[i])
temp = deepcopy(q)
answer = 0
if arr[X - 1][Y - 1] != 0:
    answer = arr[X - 1][Y - 1]
else:
    for s in range(S):

        if arr[X - 1][Y - 1] != 0:
            answer = arr[X - 1][Y - 1]
            break

        while q:
            if arr[X - 1][Y - 1] != 0:
                answer = arr[X - 1][Y - 1]
                break

            x, y = q.popleft()
            for dx, dy in (1, 0), (0, 1), (-1, 0), (0, -1):
                if 0 <= x + dx < N and 0 <= y + dy < N and arr[x + dx][y + dy] == 0:
                    arr[x+dx][y+dy] = arr[x][y]
                    temp.append((x+dx, y+dy))

        q.extend(temp)
print(answer)

