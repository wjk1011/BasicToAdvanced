n, m = int(input()), int(input())
arr = [list(map(int, input().split(' '))) for i in range(m)]
d = {i+1:[] for i in range(n)}
for i, j in arr:
    d[i].append(j)
    d[j].append(i)

stack, visited = [1], []
while True:
    if not stack:
        print(len(set(visited))-1)
        break
    now = stack.pop()
    visited.append(now)
    for i in d[now]:
        if i not in visited:
            stack.append(i)
