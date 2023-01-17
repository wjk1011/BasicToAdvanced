def solution(m, n, puddles):
    class Node:
        def __init__(self, id, loc, dist):
            self.id = id
            self.loc = loc
            self.route = 0
            self.dist = dist
    
    node_list = []        
    for x in range(1, m+1):
        for y in range(1, n+1):
            if [x,y] not in puddles:
                node_list.append(Node(((x-1) * n + y - 1),[x, y], x+y-1))
            else:
                node_list.append(Node(((x-1) * n + y - 1), [x, y], -1))
    node_list[0].route = 1

    
    for u in range(1,len(node_list)):
        if node_list[u].dist != -1:
            if node_list[u].id % n != 0 and node_list[u].id>=n:
                u_up = node_list[node_list[u].id-1]
                u_left = node_list[node_list[u].id-n]
                node_list[u].route = u_up.route + u_left.route

            elif node_list[u].id % n == 0:
                u_left = node_list[node_list[u].id-n]
                node_list[u].route = u_left.route
            elif node_list[u].id<n:
                u_up = node_list[node_list[u].id-1]
                node_list[u].route = u_up.route
    return node_list[m*n-1].route%1000000007
