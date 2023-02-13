# 풀이시간 : 1시간 30분
# 정답

import copy
from collections import Counter
n = int(input())
arr = [list(map(int, input())) for i in range(n)]

def dfs(stack, arr):
    while True:
        if not stack:
            return arr
        state = stack.pop()
        sx, sy = state[0][0], state[0][1]
        arr[sx][sy] = state[1]
        if sx + 1 < n:
            if arr[sx + 1][sy] == 1:
                stack.append([[sx + 1, sy], state[1]])
                arr[sx + 1][sy] = state[1]

        if sx - 1 >= 0:
            if arr[sx - 1][sy] == 1:
                stack.append([[sx - 1, sy], state[1]])
                arr[sx - 1][sy] = state[1]

        if sy + 1 < n:
            if arr[sx][sy + 1] == 1:
                stack.append([[sx, sy + 1], state[1]])
                arr[sx][sy + 1] = state[1]

        if sy - 1 >= 0:
            if arr[sx][sy - 1] == 1:
                stack.append([[sx, sy - 1], state[1]])
                arr[sx][sy - 1] = state[1]

m = 2
for i, column in enumerate(arr):
    for j, row in enumerate(column):
        if row == 1:
            state = [[i, j], m]
            stack = [state]
            dfs(stack, arr)
            m += 1

answer = {i:0 for i in range(2,m)}
for i in arr:
    for j in i:
        if j in answer:
            answer[j] += 1
print(len(answer))
for i in sorted(answer.values()):
    print(i)
