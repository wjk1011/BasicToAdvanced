# 정답

from collections import deque

N, M = list(map(int, input().split(' ')))
arr = [list(input()) for i in range(N)]

answer = 0
for i, c in enumerate(arr):
    for j, v in enumerate(c):
        if v == 'L':
            q = deque([(i, j)])
            dist = [[0] * M for _ in range(N)]
            dist[i][j] = 1
            while q:
                x, y = q.popleft()

                for dx, dy in (1, 0), (0, 1), (-1, 0), (0, -1):
                    if 0 <= x + dx < N and 0 <= y + dy < M and dist[x + dx][y + dy] == 0 and arr[x + dx][y + dy] == 'L':
                        dist[x + dx][y + dy] = dist[x][y] + 1
                        q.append((x + dx, y + dy))

                answer = max(answer, dist[x][y] - 1)

print(answer)
