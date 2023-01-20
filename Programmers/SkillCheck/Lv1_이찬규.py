# 1번 정답
def solution(array, commands):
    return [sorted(array[i-1:j])[k-1] for i,j,k in commands]
  
# 2번 정답
def solution(survey, choices):
    dict_sur = {'R':0,'T':0,'C':0,'F':0,'J':0,'M':0,'A':0,'N':0}
    for i in range(len(survey)):
        if choices[i] > 4:
            dict_sur[survey[i][1]] += choices[i] - 4
        elif choices[i] < 4:
            dict_sur[survey[i][0]] += 4 - choices[i]

    answer = ''
    if dict_sur['R'] - dict_sur['T'] >= 0:
        answer += 'R'
    else:
        answer += 'T'

    if dict_sur['C'] - dict_sur['F'] >= 0:
        answer += 'C'
    else:
        answer += 'F'
    if dict_sur['J'] - dict_sur['M'] >= 0:
        answer += 'J'
    else:
        answer += 'M'
    if dict_sur['A'] - dict_sur['N'] >= 0:
        answer += 'A'
    else:
        answer += 'N'
    return answer
