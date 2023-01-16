

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
