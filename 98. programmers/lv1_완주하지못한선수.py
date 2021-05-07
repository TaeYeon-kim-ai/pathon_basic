'''
수많은 마라톤 선수들이 마라톤에 참여하였습니다. 단 한 명의 선수를 제외하고는 모든 선수가 마라톤을 완주하였습니다.

마라톤에 참여한 선수들의 이름이 담긴 배열 participant와 완주한 선수들의 이름이 담긴 배열 completion이 주어질 때, 완주하지 못한 선수의 이름을 return 하도록 solution 함수를 작성해주세요.

제한사항
마라톤 경기에 참여한 선수의 수는 1명 이상 100,000명 이하입니다.
completion의 길이는 participant의 길이보다 1 작습니다.
참가자의 이름은 1개 이상 20개 이하의 알파벳 소문자로 이루어져 있습니다.
참가자 중에는 동명이인이 있을 수 있습니다.
입출력 예
participant	completion	return
["leo", "kiki", "eden"]	["eden", "kiki"]	"leo"
["marina", "josipa", "nikola", "vinko", "filipa"]	["josipa", "filipa", "marina", "nikola"]	"vinko"
["mislav", "stanko", "mislav", "ana"]	["stanko", "ana", "mislav"]	"mislav"
입출력 예 설명
예제 #1
"leo"는 참여자 명단에는 있지만, 완주자 명단에는 없기 때문에 완주하지 못했습니다.

예제 #2
"vinko"는 참여자 명단에는 있지만, 완주자 명단에는 없기 때문에 완주하지 못했습니다.

예제 #3
"mislav"는 참여자 명단에는 두 명이 있지만, 완주자 명단에는 한 명밖에 없기 때문에 한명은 완주하지 못했습니다.
'''
# def solution(participants, completions):

#     temp = []
#     for participant in participants:
#         if participant not in completions:
#             temp.append(participant)

#     return temp[0]

# result = solution(["marina", "josipa", "nikola", "vinko", "filipa"], ["josipa", "filipa", "marina", "nikola"])
# print(result)

#========================
def solution(participants, completions):
        participants.sort()
        completions.sort()
        for i, j in zip(participants, completions) :
            if i != j :
                return i
        return participants.pop()

result = solution(["marina", "josipa", "nikola", "vinko", "filipa"], ["josipa", "filipa", "marina", "nikola"])
print(result)

'''
zip : 배열을 같은 인덱스끼리 짝지어준다. 만약 배열의 길이가 다를 경우 같은 인덱스끼리만 짝지어주고, zip 객체에서 나머지 인덱스는 제외된다.

>>> a = [1,2,3,4,5]
>>> b = [1,2,3,4]
>>> zip(a,b) # zip(a,b)를 shell에 찍으면 객체 <zip object at 0x104a3e960>가 나옴 

>>> for a in zip(a,b):
...     print(a)

# a의 마지막 인덱스 5는 제외되어 있는 것을 알 수 있다.
(1, 1)
(2, 2)
(3, 3)
(4, 4)
'''

#==============================
#모범답
import collections

def solution(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    return list(answer.keys())[0]

result = solution(["marina", "josipa", "nikola", "vinko", "filipa"], ["josipa", "filipa", "marina", "nikola"])
print(result)

#=============================
#hash
def solution(participant, completion):
    answer = ''
    temp = 0
    dic = {}
    for part in participant:
        dic[hash(part)] = part
        temp += int(hash(part))
    for com in completion:
        temp -= hash(com)
    answer = dic[temp]

    return answer