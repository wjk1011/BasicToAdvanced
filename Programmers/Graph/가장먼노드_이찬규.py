# 풀이 시간 : 1시간 32분
# 정답
# 시간 초과로 애먹다가 edge를 dictionary로 바꿔서 해결

def solution(n, edge):
    class Node:
        def __init__(self, id, e):
            self.id = id
            self.depth = 50000
            self.edge = e
    
    dict_edge = {i+1:[] for i in range(n)}
    for e1,e2 in edge:
        dict_edge[e1].append(e2)
        dict_edge[e2].append(e1)
    

    node_list = [Node(i+1, dict_edge[i+1]) for i in range(n)]
    node_list[0].depth = 0
    
    
    temp = 0
    for i in range(n):
        temp_list = list(filter(lambda x:x.depth == temp, node_list))
        for t in temp_list:
            for e in t.edge:
                if node_list[e-1].depth == 50000:
                    node_list[e-1].depth = temp +1
        temp +=1
        
        if all(i.depth != 50000 for i in node_list):
            return len(list(filter(lambda x: x.depth == temp, node_list)))
