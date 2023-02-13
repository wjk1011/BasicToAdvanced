# 정답

from collections import deque
from copy import deepcopy

N, M = map(int, input().split(' '))
Hx, Hy = map(int, input().split(' '))
Ex, Ey = map(int, input().split(' '))
arr = [list(map(int, input().split(' '))) for _ in range(N)]
dist = [[[-1, -1] for _ in range(M)] for _ in range(N)]

q = deque([[Hx - 1, Hy - 1, 0]])
dist[Hx - 1][Hy - 1][0] = 0
answer = 0
while q:
    x, y, z = q.popleft()
    if x == Ex - 1 and y == Ey - 1:
        answer = dist[x][y][z]
        break

    for dx, dy in (1, 0), (-1, 0), (0, 1), (0, -1):
        nx, ny, nz = x + dx, y + dy, z
        if nx < 0 or nx >= N or ny < 0 or ny >= M:
            continue
        if arr[nx][ny]:
            if nz:
                continue
            else:
                nz = 1
        if dist[nx][ny][nz] == -1:
            dist[nx][ny][nz] = dist[x][y][z] + 1
            q.append([nx, ny, nz])
if not answer:
    print(-1)
else:
    print(answer)
