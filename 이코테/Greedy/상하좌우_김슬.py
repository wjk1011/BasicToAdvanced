# 풀이 시간 - 10분
# 정답
# 답안 예시랑 비교해보니 구현 실력 부족

N = int(input())
plan = list(input().split())
x = 1
y = 1
for i in plan:
    if(i =='R'and N >= y+1):
        y += 1
    elif(i =='L' and 1 <= y-1):
        y -= 1
    elif(i =='U' and 1 <= x-1):
        x -= 1
    elif(i =='D' and N >= x+1):
        x += 1
print(x,y)