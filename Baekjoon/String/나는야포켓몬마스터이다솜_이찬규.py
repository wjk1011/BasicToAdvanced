# 정답

N, M = list(map(int, input().split(' ')))
arr = [input() for i in range(N)]
d_pok = {}
for i, v in enumerate(arr):
    d_pok[str(i+1)] = v
    d_pok[v] = i+1
for i in range(M):
    print(d_pok[input()])
