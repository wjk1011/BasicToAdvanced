

def solution(tickets):
    dict_ticket = {}
    for i in tickets:
        if i[0] in dict_ticket:
            dict_ticket[i[0]].append(i[1])
        else:
            dict_ticket[i[0]] = [i[1]]
    for i in dict_ticket:
        dict_ticket[i].sort()
    answer = []
    stack = ['ICN']
    
    while True:
        now = stack.pop()
        answer.append(now)
        if (now not in dict_ticket) or (len(dict_ticket[now])==0):
            print(dict_ticket)
            return answer
        stack.append(dict_ticket[now][0])
        dict_ticket[now].pop(0)
        
    
