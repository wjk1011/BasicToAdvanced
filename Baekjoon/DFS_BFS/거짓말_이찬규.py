# 정답

N, M = list(map(int, input().split(' ')))
truth = list(map(int, input().split(' ')))[1:]
d_people = {i+1: [] for i in range(N)}
arr = [list(map(int, input().split(' ')))[1:] for _ in range(M)]

graph = [[0] * (N+1) for _ in range(N+1)]
visit = [False] * (N+1)
for a in arr:
    for i in a:
        for j in a:
            if i != j:
                graph[i][j] = 1

stack = truth
while stack:
    now = stack.pop()
    visit[now] = True
    for i, v in enumerate(graph[now]):
        if v == 1 and not visit[i]:
            stack.append(i)

truth = [i for i, v in enumerate(visit) if v]
cnt = 0
for a in arr:
    for p in a:
        if p in truth:
            cnt += 1
            break
print(M-cnt)
