# 1 성공
def solution(genres, plays):
    answer_list = []
    gpi = [[g, plays[i], i] for i, g in enumerate(genres)]
    dict_music = {i[0]: 0 for i in gpi}
    for i in gpi:
        dict_music[i[0]] += i[1]
    while True:
        now = list(filter(lambda x: dict_music[x]==max(dict_music.values()), dict_music))[0]
        answer = list(filter(lambda x: x[0]==now, gpi))
        del dict_music[now]
        if len(answer) > 1:
            answer = sorted(answer, key=lambda x: (-x[1],x[2]))[:2]
            for i in answer:
                answer_list.append(i[2])
        else:
            answer_list.append(answer[0][2])
        if len(dict_music) == 0:
            return answer_list


# 2 실패
# [다단계 칫솔 판매] 문제
# 테스트 케이스는 다 맞았는데 제출하니까 다 틀림 왜 틀렸는지 모르겠음
def solution(enroll, referral, seller, amount):
    dict_seller = {i:[None, [], 0, 0] for i in enroll} #부모, 자녀, 판매량, 이익
    for i, e in enumerate(enroll):
        if referral[i] != '-':
            dict_seller[e][0] = referral[i]
            dict_seller[referral[i]][1].append(e)

    for i, s in enumerate(seller):
        dict_seller[s][2] += amount[i]

    def recursive(s, dict_seller, money):
        if money > 10:
            if dict_seller[s][0] is None:
                dict_seller[s][3] += round(money * 0.9)
                return dict_seller
            else:
                dict_seller[s][3] += round(money * 0.9)
                s = dict_seller[s][0]
                money = round(money*0.1)
                recursive(s, dict_seller, money)
        else:
            dict_seller[s][3] += money
            return dict_seller
    for s in seller:
        money = dict_seller[s][2] * 100
        recursive(s, dict_seller, money)
    answer = []
    for i in enroll:
        answer.append(dict_seller[i][3])
    return answer

# 해결
# 한 사람이 칫솔 2개, 2개 팔았을 때랑 4개 팔았을 때 결과가 다르다는 것을 간과함
import math
def solution(enroll, referral, seller, amount):
    dict_seller = {i:[None,  0, 0] for i in enroll} #부모, 판매량, 이익
    for i, e in enumerate(enroll):
        if referral[i] != '-':
            dict_seller[e][0] = referral[i]
            
    def recursive(s, dict_seller, money):
        if money >= 10:
            if dict_seller[s][0] is None:
                dict_seller[s][2] += money - math.floor(money * 0.1)
                return dict_seller
            else:
                dict_seller[s][2] += money - math.floor(money * 0.1)
                s = dict_seller[s][0]
                money = math.floor(money * 0.1)
                recursive(s, dict_seller, money)
        else:
            dict_seller[s][2] += money
            return dict_seller
    for i, s in enumerate(seller):
        money = amount[i] * 100
        recursive(s, dict_seller, money)
    answer = [dict_seller[i][2] for i in enroll]
    return answer
