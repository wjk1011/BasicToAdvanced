# 풀이 시간 : 1시간 5분
# 정답


def solution(begin, target, words):
    n = len(begin)
    stack = [[begin,0]]

    visited = []
    while True:

        if len(stack) == 0:
            answer = list(filter(lambda x: x[0]==target, visited))

            if len(answer) == 0:
                return 0
            else:
                answer = min(list(map(lambda x: x[1], answer)))
                return answer

        now = stack.pop()
        for w in words:
            check = 0
            for i in range(len(now[0])):
                
                if w[i] == now[0][i]:
                    check += 1
                    
            if check == n-1:

                check = 0
                
                compare = list(filter(lambda x: w == x[0], visited))
                if len(compare) != 0:
                    for c in compare:
                        if c[1] > now[1]+1:
                            stack.append([w,now[1]+1])
                            visited.append([w,now[1]+1])
                else:
                    stack.append([w,now[1]+1])
                    visited.append([w,now[1]+1])
                            
        
        
