'''
문제 설명
수많은 마라톤 선수들이 마라톤에 참여하였습니다. 단 한 명의 선수를 제외하고는 모든 선수가 마라톤을 완주하였습니다.
마라톤에 참여한 선수들의 이름이 담긴 배열 participant와 완주한 선수들의 이름이 담긴 배열 completion이 주어질 때, 
완주하지 못한 선수의 이름을 return 하도록 solution 함수를 작성해주세요.

제한사항
마라톤 경기에 참여한 선수의 수는 1명 이상 100,000명 이하입니다.
completion의 길이는 participant의 길이보다 1 작습니다.
참가자의 이름은 1개 이상 20개 이하의 알파벳 소문자로 이루어져 있습니다.
참가자 중에는 동명이인이 있을 수 있습니다.
'''

# 1
import collections

def solution(participant, completion):
    result = collections.Counter(participant) - collections.Counter(completion)
    return list(result)[0]

# 2
def solution(participant, completion):
    participant.sort()
    completion.sort()
    for par, com in zip(participant, completion):
        if par != com:
            return par
    return participant[-1]

# 3
def solution(participant, completion):
    dic = {}
    temp = 0
    for par in participant:
        dic[hash(par)] = par
        temp += hash(par)
    for com in completion:
        temp -= hash(com)
    answer = dic[temp]
    return answer

participant = ["leo", "kiki", "eden"]
completion = ["eden", "kiki"]
solution(participant, completion)   # "leo"