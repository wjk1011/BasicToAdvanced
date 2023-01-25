# 풀이 시간 기록을 못했음 꽤 걸린거같음
# 정답

n, m, v = map(int, input().split(' '))
arr = [list(map(int, input().split(' '))) for _ in range(m)]

d = {i+1: [] for i in range(n)}
for i, j in arr:
    d[i].append(j)
    d[j].append(i)

d = {i: sorted(d[i]) for i in d}
answer = ''
stack, visited = [v], []
while True:
    if not stack:
        for i in visited:
            answer += str(i) + ' '
        print(answer)
        break
    now = stack.pop()
    if now not in visited:
        visited.append(now)
        next = len(d[now])
        for i in range(next):
            _ = d[now].pop()
            if _ not in visited:
                stack.append(_)

d = {i+1: [] for i in range(n)}
for i, j in arr:
    d[i].append(j)
    d[j].append(i)

d = {i: sorted(d[i], reverse=True) for i in d}
answer = ''
stack, visited = [v], []
while True:
    if not stack:
        for i in visited:
            answer += str(i) + ' '
        print(answer)
        break
    now = stack.pop(0)
    visited.append(now)
    next = len(d[now])
    for i in range(next):
        _ = d[now].pop()
        if _ not in visited and _ not in stack:
            stack.append(_)
