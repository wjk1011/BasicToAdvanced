# 시간 초과 실패

N, M = list(map(int, input().split(' ')))
arr = [list(map(int, input().split(' '))) for i in range(M)]
d = {i+1: [] for i in range(N)}
for x, y in arr:
    d[x].append(y)
    d[y].append(x)

_visited = {i+1:False for i in range(N)}
answer = [[0]]
for i in range(1, N+1):
    if _visited[i]:
        continue
    else:
        stack, visited = [i], {j+1: False for j in range(N)}
        while stack:
            now = stack.pop()
            if visited[now]:
                continue
            else:
                visited[now] = True
                _visited[now] = True
                stack.extend(list(filter(lambda x: not visited[x], d[now])))
        answer.append(visited)

print(len(answer)-1)
