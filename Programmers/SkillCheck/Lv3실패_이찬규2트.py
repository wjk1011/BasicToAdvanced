# 1
# #2 먼저 풀다가 문제 읽어보지도 못함

# 2
# 억억단 
#시간초과 해결 못함

def solution(e, starts):
    answer = []
    for s in starts:
        n, m = 1, 1
        dict_num = {i:0 for i in range(s, e+1)}
        while True:
            if n * m > e:
                n += 1
                m = n+1

            else:
                if n*m in dict_num:
                    dict_num[n*m] += 1
                m += 1
            
            if n == e+1:
                for i in dict_num:
                    if dict_num[i] == max(dict_num.values()):
                        answer.append(i)
                        break
                break
                
            
    return answer
