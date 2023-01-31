# 정답

from collections import deque

t = int(input())
for i in range(t):
    n = int(input())
    hx, hy = list(map(int, input().split(' ')))
    store = [list(map(int, input().split(' '))) for _ in range(n)]
    fx, fy = list(map(int, input().split(' ')))
    answer = 'sad'
    q, visited = deque([[hx, hy]]), []
    while q:
        x, y = q.popleft()
        if abs(fx - x) + abs(fy - y) <= 1000:
            answer = 'happy'
            break

        else:
            next = list(filter(lambda s:abs(s[0] - x) + abs(s[1] - y) <= 1000 and s not in visited, store))
            q.extend(next)
            visited.extend(next)

    print(answer)
