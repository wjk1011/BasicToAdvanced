# 정답

from collections import deque

T = int(input())
for _ in range(T):
    N, M = list(map(int, input().split(' ')))
    arr = list(map(int, input().split(' ')))

    q = deque(list(map(lambda x: [arr[x], x], range(len(arr)))))
    n = 0
    if N == 1:
        print(1)
    else:
        while q:
            now = q.popleft()
            if not q:
                n += 1
                break
            else:
                if now[0] >= max(list(map(lambda x: x[0], q))):
                    n += 1
                    if now[1] == M:
                        break

                else:
                    q.append(now)
        print(n)
