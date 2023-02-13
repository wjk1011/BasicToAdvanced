# 정답

from collections import deque
T = int(input())
for _ in range(T):
    l = int(input())
    arr = [[0] * l for i in range(l)]
    q = deque([list(map(int, input().split(' ')))])
    ox, oy = list(map(int, input().split(' ')))
    if [ox, oy] == q[0]:
        print(0)
    else:
        while q:
            now = q.popleft()
            nx, ny = now[0], now[1]
            dx, dy = [-1, -2, -2, -1, 1, 2, 2, 1], [-2, -1, 1, 2, -2, -1, 1, 2]
            for next in range(8):
                if (0 <= nx + dx[next] <= l - 1) and (0 <= ny + dy[next] <= l - 1):
                    if arr[nx + dx[next]][ny + dy[next]] == 0:
                        if ox == nx + dx[next] and oy == ny + dy[next]:
                            arr[nx + dx[next]][ny + dy[next]] = arr[nx][ny] + 1
                            break
                        else:
                            q.append([nx + dx[next], ny + dy[next]])
                            arr[nx + dx[next]][ny + dy[next]] = arr[nx][ny] + 1

            if arr[ox][oy] != 0:
                print(arr[ox][oy])
                break
