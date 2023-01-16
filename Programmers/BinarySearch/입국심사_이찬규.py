# 풀이시간 : 2시간 46분
# 정답

def solution(n, times):
    start, end = 0, max(times) * n
    while True:
        target = (start + end) // 2
        if sum([target // i for i in times]) >= n:
            end = (start + end) // 2
                
        elif sum([target // i for i in times]) < n:
            if start == (start + end) // 2:
                return end
            else:
                start = (start + end) // 2

