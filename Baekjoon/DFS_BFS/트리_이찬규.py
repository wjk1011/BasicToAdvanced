# 정답

N = int(input())
arr = list(map(int, input().split(' ')))
eli = int(input())


def dfs(num, arr):
    arr[num] = -2
    for i, v in enumerate(arr):
        if num == v:
            dfs(i, arr)


dfs(eli, arr)
cnt = 0
for i, v in enumerate(arr):
    if v != -2 and i not in arr:
        cnt += 1
print(cnt)
