# 정답

from collections import deque
while True:
    w, h = list(map(int, input().split(' ')))
    if w + h == 0:
        break
    else:
        arr = [list(map(int, input().split(' '))) for _ in range(h)]

        dx, dy = [-1, -1, -1, 0, 0, 1, 1, 1], [-1, 0, 1, -1, 1, -1, 0, 1]
        n = 2
        for i, c in enumerate(arr):
            for j, v in enumerate(c):
                if v == 1:
                    q = deque([[i, j]])

                    while q:
                        now = q.popleft()
                        nx, ny = now[0], now[1]
                        arr[nx][ny] = n
                        for next in range(8):
                            if 0 <= nx + dx[next] <= h - 1 and 0 <= ny + dy[next] <= w - 1:
                                if arr[nx + dx[next]][ny + dy[next]] == 1:
                                    q.append([nx + dx[next], ny + dy[next]])
                                    arr[nx + dx[next]][ny + dy[next]] = n
                    n += 1
        print(n-2)

