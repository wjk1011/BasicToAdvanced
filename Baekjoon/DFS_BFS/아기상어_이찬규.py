# 정답

from collections import deque


class Baby:
    def __init__(self):
        self.level = 2
        self.eaten = 0
        self.location = (-1, -1)


N = int(input())
arr = [list(map(int, input().split(' '))) for _ in range(N)]

baby_idx = [[i, j] for i in range(N) for j in range(N) if arr[i][j] == 9][0]
baby_idx.append(0)
baby = Baby()
q = deque([baby_idx])
arr[baby_idx[0]][baby_idx[1]] = 0
dist = [[0] * N for _ in range(N)]
eatable = []
answer = 0
while True:
    while q:
        x, y, z = q.popleft()
        for dx, dy in (-1, 0), (0, -1), (1, 0), (0, 1):
            if 0 <= x + dx < N and 0 <= y + dy < N and dist[x + dx][y + dy] == 0 and arr[x + dx][y + dy] <= baby.level:
                if 0 < arr[x + dx][y + dy] < baby.level:
                    eatable.append((x + dx, y + dy, z + 1))
                else:
                    q.append((x + dx, y + dy, z + 1))
                    dist[x + dx][y + dy] = 1

    if eatable:
        eatable = sorted(eatable, key=lambda x: (x[2], x[0], x[1]))[0]
        baby.eaten += 1
        if baby.eaten == baby.level:
            baby.eaten = 0
            baby.level += 1
        eatable = list(eatable)
        answer += eatable[-1]
        eatable[-1] = 0
        q = deque([tuple(eatable)])
        arr[eatable[0]][eatable[1]] = 0
        eatable = []
        dist = [[0] * N for _ in range(N)]

    else:
        print(answer)
        break
