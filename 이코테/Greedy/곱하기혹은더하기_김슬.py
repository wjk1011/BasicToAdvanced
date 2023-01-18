# 풀이시간 : 10분
# 정답

S = input()
result = 1

for i in S:
    if(i == '0'):
        pass
    elif(i == '1'):
        result += 1
    else:
        result *= int(i)
print(result)