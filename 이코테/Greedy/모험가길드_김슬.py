N = int(input())
fear = sorted(list(map(int, input().split())))
cnt = 0

for i in range(len(fear)):
    if(N < fear[i] or N <= max(fear[i:])):
        print(cnt)
        break
    N -= fear[i]
    cnt += 1
    
