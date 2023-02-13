# 시간초과를 해결할 방법을 모르겠어서 정답 코드 가져옴
# 밑에 다시 풀거임

#내꺼
w, h = list(map(int, input().split(' ')))
arr = [list(input()) for i in range(h)]
for i, c in enumerate(arr):
    for j, r in enumerate(c):
        if r == '.':
            arr[i][j] = 0
answer = []
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]  # up down left right
start_end = []
for i, c in enumerate(arr):
    for j, r in enumerate(c):
        if r == 'C':
            start_end.append([i, j])
            arr[i][j] = 0

start, end = start_end
q = [[start, ' ']]
while q:
    now = q.pop()
    if answer and min(answer) > arr[now[0][0]][now[0][1]]:
        nx, ny = now[0][0], now[0][1]
        for d in range(4):
            if 0 <= nx + dx[d] < h and 0 <= ny + dy[d] < w and arr[nx + dx[d]][ny + dy[d]] != '*':
                if d == 0:  # up
                    next = [[nx + dx[d], ny + dy[d]], 'up']
                    if now[1] != 'up':
                        if arr[next[0][0]][next[0][1]] != 0:
                            if arr[nx][ny] + 1 <= arr[next[0][0]][next[0][1]]:
                                arr[next[0][0]][next[0][1]] = arr[nx][ny] + 1
                                q.append(next)

                        else:
                            arr[next[0][0]][next[0][1]] = arr[nx][ny] + 1
                            q.append(next)
                        if next[0] == end:
                            answer.append(arr[end[0]][end[1]] - 1)
                    else:
                        if arr[next[0][0]][next[0][1]] != 0:
                            if arr[nx][ny] <= arr[next[0][0]][next[0][1]]:
                                arr[next[0][0]][next[0][1]] = arr[nx][ny]
                                q.append(next)
                        else:
                            arr[next[0][0]][next[0][1]] = arr[nx][ny]
                            q.append(next)
                        if next[0] == end:
                            answer.append(arr[end[0]][end[1]] - 1)

                elif d == 1:  # down
                    next = [[nx + dx[d], ny + dy[d]], 'down']
                    if now[1] != 'down':
                        next[1] = 'down'
                        if arr[next[0][0]][next[0][1]] != 0:
                            if arr[nx][ny] + 1 <= arr[next[0][0]][next[0][1]]:
                                arr[next[0][0]][next[0][1]] = arr[nx][ny] + 1
                                q.append(next)
                        else:
                            arr[next[0][0]][next[0][1]] = arr[nx][ny] + 1
                            q.append(next)
                        if next[0] == end:
                            answer.append(arr[end[0]][end[1]] - 1)
                    else:
                        if arr[next[0][0]][next[0][1]] != 0:
                            if arr[nx][ny] <= arr[next[0][0]][next[0][1]]:
                                arr[next[0][0]][next[0][1]] = arr[nx][ny]
                                q.append(next)
                        else:
                            arr[next[0][0]][next[0][1]] = arr[nx][ny]
                            q.append(next)
                        if next[0] == end:
                            answer.append(arr[end[0]][end[1]] - 1)

                elif d == 2:  # left
                    next = [[nx + dx[d], ny + dy[d]], 'left']
                    if now[1] != 'left':
                        next[1] = 'left'
                        if arr[next[0][0]][next[0][1]] != 0:
                            if arr[nx][ny] + 1 <= arr[next[0][0]][next[0][1]]:
                                arr[next[0][0]][next[0][1]] = arr[nx][ny] + 1
                                q.append(next)
                        else:
                            arr[next[0][0]][next[0][1]] = arr[nx][ny] + 1
                            q.append(next)
                        if next[0] == end:
                            answer.append(arr[end[0]][end[1]] - 1)
                    else:
                        if arr[next[0][0]][next[0][1]] != 0:
                            if arr[nx][ny] <= arr[next[0][0]][next[0][1]]:
                                arr[next[0][0]][next[0][1]] = arr[nx][ny]
                                q.append(next)
                        else:
                            arr[next[0][0]][next[0][1]] = arr[nx][ny]
                            q.append(next)
                        if next[0] == end:
                            answer.append(arr[end[0]][end[1]] - 1)

                elif d == 3:  # right
                    next = [[nx + dx[d], ny + dy[d]], 'right']
                    if now[1] != 'right':
                        next[1] = 'right'
                        if arr[next[0][0]][next[0][1]] != 0:
                            if arr[nx][ny] + 1 <= arr[next[0][0]][next[0][1]]:
                                arr[next[0][0]][next[0][1]] = arr[nx][ny] + 1
                                q.append(next)
                        else:
                            arr[next[0][0]][next[0][1]] = arr[nx][ny] + 1
                            q.append(next)
                        if next[0] == end:
                            answer.append(arr[end[0]][end[1]] - 1)
                    else:
                        if arr[next[0][0]][next[0][1]] != 0:
                            if arr[nx][ny] <= arr[next[0][0]][next[0][1]]:
                                arr[next[0][0]][next[0][1]] = arr[nx][ny]
                                q.append(next)
                        else:
                            arr[next[0][0]][next[0][1]] = arr[nx][ny]
                            q.append(next)

                        if next[0] == end:
                            answer.append(arr[end[0]][end[1]] - 1)
    else:
        nx, ny = now[0][0], now[0][1]
        for d in range(4):
            if 0 <= nx + dx[d] < h and 0 <= ny + dy[d] < w and arr[nx + dx[d]][ny + dy[d]] != '*':

                if d == 0:  # up
                    next = [[nx + dx[d], ny + dy[d]], 'up']
                    if now[1] != 'up':
                        if arr[next[0][0]][next[0][1]] != 0:
                            if arr[nx][ny] + 1 <= arr[next[0][0]][next[0][1]]:
                                arr[next[0][0]][next[0][1]] = arr[nx][ny] + 1
                                q.append(next)

                        else:
                            arr[next[0][0]][next[0][1]] = arr[nx][ny] + 1
                            q.append(next)
                        if next[0] == end:
                            answer.append(arr[end[0]][end[1]] - 1)
                    else:
                        if arr[next[0][0]][next[0][1]] != 0:
                            if arr[nx][ny] <= arr[next[0][0]][next[0][1]]:
                                arr[next[0][0]][next[0][1]] = arr[nx][ny]
                                q.append(next)
                        else:
                            arr[next[0][0]][next[0][1]] = arr[nx][ny]
                            q.append(next)
                        if next[0] == end:
                            answer.append(arr[end[0]][end[1]] - 1)

                elif d == 1:  # down
                    next = [[nx + dx[d], ny + dy[d]], 'down']
                    if now[1] != 'down':
                        next[1] = 'down'
                        if arr[next[0][0]][next[0][1]] != 0:
                            if arr[nx][ny] + 1 <= arr[next[0][0]][next[0][1]]:
                                arr[next[0][0]][next[0][1]] = arr[nx][ny] + 1
                                q.append(next)
                        else:
                            arr[next[0][0]][next[0][1]] = arr[nx][ny] + 1
                            q.append(next)
                        if next[0] == end:
                            answer.append(arr[end[0]][end[1]] - 1)
                    else:
                        if arr[next[0][0]][next[0][1]] != 0:
                            if arr[nx][ny] <= arr[next[0][0]][next[0][1]]:
                                arr[next[0][0]][next[0][1]] = arr[nx][ny]
                                q.append(next)
                        else:
                            arr[next[0][0]][next[0][1]] = arr[nx][ny]
                            q.append(next)
                        if next[0] == end:
                            answer.append(arr[end[0]][end[1]] - 1)

                elif d == 2:  # left
                    next = [[nx + dx[d], ny + dy[d]], 'left']
                    if now[1] != 'left':
                        next[1] = 'left'
                        if arr[next[0][0]][next[0][1]] != 0:
                            if arr[nx][ny] + 1 <= arr[next[0][0]][next[0][1]]:
                                arr[next[0][0]][next[0][1]] = arr[nx][ny] + 1
                                q.append(next)
                        else:
                            arr[next[0][0]][next[0][1]] = arr[nx][ny] + 1
                            q.append(next)
                        if next[0] == end:
                            answer.append(arr[end[0]][end[1]] - 1)
                    else:
                        if arr[next[0][0]][next[0][1]] != 0:
                            if arr[nx][ny] <= arr[next[0][0]][next[0][1]]:
                                arr[next[0][0]][next[0][1]] = arr[nx][ny]
                                q.append(next)
                        else:
                            arr[next[0][0]][next[0][1]] = arr[nx][ny]
                            q.append(next)
                        if next[0] == end:
                            answer.append(arr[end[0]][end[1]] - 1)

                elif d == 3:  # right
                    next = [[nx + dx[d], ny + dy[d]], 'right']
                    if now[1] != 'right':
                        next[1] = 'right'
                        if arr[next[0][0]][next[0][1]] != 0:
                            if arr[nx][ny] + 1 <= arr[next[0][0]][next[0][1]]:
                                arr[next[0][0]][next[0][1]] = arr[nx][ny] + 1
                                q.append(next)
                        else:
                            arr[next[0][0]][next[0][1]] = arr[nx][ny] + 1
                            q.append(next)
                        if next[0] == end:
                            answer.append(arr[end[0]][end[1]] - 1)
                    else:
                        if arr[next[0][0]][next[0][1]] != 0:
                            if arr[nx][ny] <= arr[next[0][0]][next[0][1]]:
                                arr[next[0][0]][next[0][1]] = arr[nx][ny]
                                q.append(next)
                        else:
                            arr[next[0][0]][next[0][1]] = arr[nx][ny]
                            q.append(next)

                        if next[0] == end:
                            answer.append(arr[end[0]][end[1]] - 1)

print(min(answer))

#정답 코드
from sys import stdin
from collections import deque
input = stdin.readline

w, h = map(int, input().split())
a = [list(input().strip()) for _ in range(h)]
dist = [[0]*w for _ in range(h)]
q = deque()
ex, ey = -1, 0

def bfs():
    while q:
        x, y = q.popleft()
        for dx, dy in (-1, 0), (1, 0), (0, -1), (0, 1):
            nx, ny = x+dx, y+dy
            while 0 <= nx < h and 0 <= ny < w and a[nx][ny] != '*':
                if not dist[nx][ny]:
                    dist[nx][ny] = dist[x][y]+1
                    q.append((nx, ny))
                nx, ny = nx+dx, ny+dy

for i in range(h):
    for j in range(w):
        if a[i][j] == 'C':
            if ex == -1:
                ex, ey = i, j
            else:
                q.append((i, j))
bfs()
print(dist[ex][ey]-1)

#
