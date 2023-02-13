# 정답

from collections import deque

N, L, R = list(map(int, input().split(' ')))
arr = [list(map(int, input().split(' '))) for _ in range(N)]
arr_idx = [(i, j) for i in range(N) for j in range(N)]

answer = 0
while True:
    union = [[False for j in range(N)] for i in range(N)]
    check = 0
    for idx in arr_idx:
        if not union[idx[0]][idx[1]]:
            q, visit = deque([idx]), [idx]

            while q:
                x, y = q.popleft()
                union[x][y] = True
                for dx, dy in (1, 0), (-1, 0), (0, 1), (0, -1):
                    if 0 <= x + dx < N and 0 <= y + dy < N and not union[x+dx][y+dy] and (x + dx, y + dy) not in visit and L <= abs(arr[x][y] - arr[x + dx][y + dy]) <= R:
                        q.append((x + dx, y + dy))
                        visit.append((x + dx, y + dy))
                        union[x + dx][y + dy] = True
            if len(visit) == 1:
                check += 1

            move = sum(list(map(lambda x: arr[x[0]][x[1]], visit))) / len(visit)
            for x, y in visit:
                arr[x][y] = int(move)
    answer += 1
    if check == N * N:
        print(answer-1)
        break
