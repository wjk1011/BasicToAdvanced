# 풀이 시간 - 10분
# 정답

def solution(triangle):
    while True:
        if len(triangle) == 1:
            break

        bottom = triangle[-1]
        triangle.pop()
        for i in range(len(triangle[-1])):
            triangle[-1][i] += max(bottom[i], bottom[i+1])


    return triangle[0][0]
