# 정답

from collections import deque

N = int(input())
if N == 1:
    print(0)
else:
    arr = [list(map(int, input().split())) for _ in range(N - 1)]

    d_tree = {i + 1: {} for i in range(N)}
    for i, j, dist in arr:
        d_tree[i].update({j: dist})
        d_tree[j].update({i: dist})

    start = 1
    distance = [0] * (N + 1)
    visit = [False] * (N + 1)


    def bfs(start):
        visit[start] = True
        q = deque()
        q.append(start)
        while q:
            now = q.popleft()
            for i in d_tree[now]:
                if not visit[i]:
                    q.append(i)
                    visit[i] = True
                    distance[i] = distance[now] + d_tree[now][i]


    bfs(start)
    start = distance.index(max(distance))
    distance = [0] * (N + 1)
    visit = [False] * (N + 1)
    bfs(start)
    print(max(distance))
