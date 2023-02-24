# 정답

from collections import deque

t = int(input())

for i in range(t):
    p = input()
    n = int(input())
    arr = input()[1:-1].split(',')

    q = deque(arr)

    f = 0

    if n == 0:
        q = []

    for j in p:
        if j == 'R':
            f += 1
        elif j == 'D':
            if len(q) == 0:
                print("error")
                break
            else:
                if f % 2 == 0:
                    q.popleft()
                else:
                    q.pop()

    else:
        if f % 2 == 0:
            print("[" + ",".join(q) + "]")
        else:
            q.reverse()
            print("[" + ",".join(q) + "]")
