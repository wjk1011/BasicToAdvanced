# 정답

from copy import deepcopy

N, M = input(), int(input())
if M == 0:
    print(min(abs(int(N) - 100), len(N)))
elif M == 10:
    faulty = list(map(int, input().split(' ')))
    print(abs(int(N) - 100))
else:
    faulty = list(map(int, input().split(' ')))
    normal = [str(i) for i in range(10) if i not in faulty]
    combine = ['']
    answer = []
    while combine:
        now = combine.pop()
        for n in normal:
            temp = deepcopy(now)
            temp += str(n)

            if len(N) - 1 <= len(temp) <= len(N):
                answer.append(temp)

            if len(temp) <= len(N):
                combine.append(temp)

    normal = list(map(int, normal))
    if min(normal) != 0:
        add = str(min(normal)) * (len(N)+1)
    else:
        if len(normal) != 1:
            normal.remove(0)
            add = str(min(normal)) + '0' * (len(N))
        else:
            add = '0'
    answer.append(add)
    print(min(min(list(map(lambda x: abs(int(x) - int(N)) + len(x), answer))), abs(int(N) - 100)))
