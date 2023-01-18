# 풀이시간 : 5분
# 정답

S = sorted(input())
sum = 0
S_1 = S.copy()
for i in S_1:
    if(i.isalpha()):
        continue
    else:
        sum += int(i)
        S.remove(i)

print("".join(S) + str(sum))