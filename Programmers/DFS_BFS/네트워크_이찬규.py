# 풀이 시간 - 1시간 33분
# 정답
# DFS/BFS 할 줄 몰라서 머리 굴려가며 풀었는데 계속 틀렸습니다 뜸, 질문하기에 있는 테스트케이스 다 맞았다는데 왜 틀렸을까 고민해보니 line 21: 처럼 x를 set(x)로 고치니 풀림 

def solution(n, computers):
    visited = []
    for i in range(n):
        visit = [i]
        route = []
        while True:
            search = visit[-1]
            route.append(search)
            visit.pop()
            for c in range(len(computers)):
                if (computers[search][c] == 1) and (c not in route):
                    visit.append(c)
            if len(visit) == 0:
                break
        visited.append(route)
    
    visited = list(map(lambda x:sorted(set(x)), visited))

    answer = []
    for i in range(len(visited)):
        if visited[i] not in answer:
            answer.append(visited[i])
    
    return len(answer)
