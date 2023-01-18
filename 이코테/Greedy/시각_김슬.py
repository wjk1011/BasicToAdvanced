# 풀이 시간 - 5분
# 정답

N = int(input())
H, M, S, cnt = 0, 0, 0, 0
while(H < N):
    S += 1
    if(S == 60):
        M += 1
        S = 0
        if(M == 60):
            H += 1
            M = 0
    print(H,M,S)
    if('3' in str(H) + str(M) + str(S)):
        cnt += 1
print(cnt)
