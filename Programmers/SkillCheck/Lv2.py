# 풀이 시간 : 총 20분

# 1번 정답
def solution(A,B):
    answer = 0
    A = sorted(A, reverse=True)
    B = sorted(B)
    for i, _ in enumerate(A):
        answer += A[i] * B[i]
    return answer
  
# 2번 정답
  
  def solution(priorities, location):
    priorities = list(map(lambda x: [priorities[x], x], range(len(priorities))))
    cnt = 1
    while True:
        
        pri = list(map(lambda x: x[0], priorities))
        idx = list(map(lambda x: x[1], priorities))
        if pri[0] == max(pri):
            if idx[0] == location:
                return cnt
            else:
                priorities.pop(0)
                cnt += 1
        else:
            unpri = priorities.pop(0)
            priorities.append(unpri)

    return cnt
