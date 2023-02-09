# 정답

N, M = list(map(int, input().split(' ')))
arr = [i for i in range(N + 1)]
idx = 0

def recursive(answer):
    if len(answer) == M:
        print(*answer)
        return

    for i in range(1, N + 1):
        if not answer or answer[-1] <= i:
            answer.append(arr[i])
            recursive(answer)
            answer.pop()


recursive([])
