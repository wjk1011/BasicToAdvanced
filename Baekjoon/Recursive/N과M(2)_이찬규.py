# 정답

N, M = list(map(int, input().split(' ')))
arr = [i for i in range(N + 1)]
idx = 0
visit = [False] * (len(arr) + 1)


def recursive(answer):
    if len(answer) == M:
        print(*answer)
        return

    for i in range(1, N + 1):
        if not visit[i] and (not answer or answer[-1] < i):
            visit[i] = True
            answer.append(arr[i])
            recursive(answer)
            visit[i] = False
            answer.pop()


recursive([])
