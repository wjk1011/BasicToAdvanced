# 풀이시간 : 10분
# 정답

N, K = map(int,input().split())
cnt = 0
while(1):
    if(N % K != 0):
        N-= 1
    else: 
        N /= K
        cnt+=1
    if(N == 1):
        print(cnt)
        break