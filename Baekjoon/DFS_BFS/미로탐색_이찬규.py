# 정답

from collections import deque

N, M = list(map(int, input().split(' ')))
arr = [list(map(int, input())) for i in range(N)]

q = deque([[0, 0]])
dx, dy = [1,-1, 0, 0], [0, 0, 1, -1]
while q:
    now = q.popleft()
    nx, ny = now[0], now[1]
    for next in range(4):
        if 0 <= nx + dx[next] <= N-1 and 0 <= ny + dy[next] <= M-1:
            if arr[nx + dx[next]][ny + dy[next]] == 1:
                q.append([nx + dx[next], ny + dy[next]])
                arr[nx + dx[next]][ny + dy[next]] = arr[nx][ny] + 1
    if arr[N-1][M-1] != 1:
        print(arr[N-1][M-1])
        break
