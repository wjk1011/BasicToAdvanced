# 풀이 시간 : 10분
# 정답

T = int(input())
for i in range(T):
    M, N, K = list(map(int, input().split(' ')))
    arr = [[0] * M for _ in range(N)]
    for i in range(K):
        x, y = list(map(int, input().split(' ')))
        arr[y][x] = 1

    def dfs(stack, arr):
        while True:
            if not stack:
                return arr
            state = stack.pop()
            sx, sy = state[0][0], state[0][1]
            arr[sx][sy] = state[1]
            if sx + 1 < N:
                if arr[sx + 1][sy] == 1:
                    stack.append([[sx + 1, sy], state[1]])
                    arr[sx + 1][sy] = state[1]

            if sx - 1 >= 0:
                if arr[sx - 1][sy] == 1:
                    stack.append([[sx - 1, sy], state[1]])
                    arr[sx - 1][sy] = state[1]

            if sy + 1 < M:
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
    print(m-2)
