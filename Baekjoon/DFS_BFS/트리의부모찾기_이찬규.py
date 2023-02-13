# 정답

N = int(input())
arr = [list(map(int, input().split(' '))) for i in range(N-1)]

d_node, d_p = {i+1: [] for i in range(N)}, {i+1: 0 for i in range(N)}
for x,y in arr:
    d_node[x].append(y)
    d_node[y].append(x)

stack = [1]
while stack:
    now = stack.pop()
    child = list(filter(lambda x: d_p[x] == 0, d_node[now]))
    for c in child:
        d_p[c] = now
    stack.extend(child)

for i in d_p:
    if i != 1:
        print(d_p[i])
