# 정답

from collections import deque
import sys

input = sys.stdin.readline

# N = int(input())
# arr = [list(map(int, input().strip().split()))[:-1] for _ in range(N)]
# d_tree = [[] for _ in range(N)]
#
# for i, a in enumerate(arr):
#     for j in range(int(len(a[1:]) / 2)):
#         d_tree[a[0] - 1].append((a[1:][j * 2], a[1:][j * 2 + 1]))
N = int(input())
adjacent = [ [] for _ in range(N+1) ]
for i in range(1,N+1):
    req = list(map(int , input().strip().split()))
    index = 0
    S1 = req[index]
    index+=1
    while True:
        S2 = req[index]
        if S2 == -1:
            break
        E = req[index+1]
        adjacent[S1].append((S2,E))
        index+=2
distance = [0] * N
visit = [False] * N

def bfs(idx):
    q = deque()
    q.append(idx)
    visit[idx - 1] = True
    while q:
        now = q.popleft()
        for i, v in adjacent[now]:
            if not visit[i - 1]:
                q.append(i)
                visit[i - 1] = True
                distance[i - 1] = distance[now - 1] + v


bfs(1)
max_index = distance.index(max(distance)) + 1
distance = [0] * N
visit = [False] * N
bfs(max_index)
print(max(distance))
