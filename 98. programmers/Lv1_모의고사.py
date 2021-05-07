'''
수포자는 수학을 포기한 사람의 준말입니다. 수포자 삼인방은 모의고사에 수학 문제를 전부 찍으려 합니다. 수포자는 1번 문제부터 마지막 문제까지 다음과 같이 찍습니다.

1번 수포자가 찍는 방식: 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, ...
2번 수포자가 찍는 방식: 2, 1, 2, 3, 2, 4, 2, 5, 2, 1, 2, 3, 2, 4, 2, 5, ...
3번 수포자가 찍는 방식: 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, ...

1번 문제부터 마지막 문제까지의 정답이 순서대로 들은 배열 answers가 주어졌을 때, 가장 많은 문제를 맞힌 사람이 누구인지 배열에 담아 return 하도록 solution 함수를 작성해주세요.

제한 조건
시험은 최대 10,000 문제로 구성되어있습니다.
문제의 정답은 1, 2, 3, 4, 5중 하나입니다.
가장 높은 점수를 받은 사람이 여럿일 경우, return하는 값을 오름차순 정렬해주세요.
입출력 예
answers	return
[1,2,3,4,5]	[1]
[1,3,2,4,2]	[1,2,3]
입출력 예 설명
입출력 예 #1

수포자 1은 모든 문제를 맞혔습니다.
수포자 2는 모든 문제를 틀렸습니다.
수포자 3은 모든 문제를 틀렸습니다.
따라서 가장 문제를 많이 맞힌 사람은 수포자 1입니다.

입출력 예 #2

모든 사람이 2문제씩을 맞췄습니다.
'''
'''
def solution(answers):
    answer = []
    answer_temp = []
    cnt_a = 0
    cnt_b = 0
    cnt_c = 0

    a = [1, 2, 3, 4, 5] #5
    b = [2, 1, 2, 3, 2, 4, 2, 5] # 8
    c = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] # 10
    for i in range(len(answers)):
        if answers[i] == a[i%len(a)] :
            cnt_a += 1
        if answers[i] == b[i%len(b)] :
            cnt_b += 1
        if answers[i] == b[i%len(c)] :
            cnt_c += 1
    answer_temp = [cnt_a, cnt_b, cnt_c] 
    
    for person, score in enumerate(answer_temp):
        if score == max(answer_temp) :
            answer.append(person+1)
    
    return answer


리스트가 있는 경우 순서와 리스트의 값을 전달하는 함수 
순서가 있는 자료형(list, set, tuple, dictionary, string)을 입력받아 인덱스 값을 포함하는
enumerate 객체 리턴 
보통 enumerate 함수는 for문과 함께 자주 사용

출처: https://wooaoe.tistory.com/65 [개발개발 울었다]


test = [1,2,3] 
for index, value in enumerate(test): 
    print(index,value)
'''

#===========================

def solution(answers):

    cnt_a = 0
    cnt_b = 0
    cnt_c = 0

    a = [1, 2, 3, 4, 5] #5
    b = [2, 1, 2, 3, 2, 4, 2, 5] # 8
    c = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] # 10

    for i in range(len(answers)) :
        s1 = i%len(a)
        s2 = i%len(b)
        s3 = i%len(c)

        if a[s1] == answers[i]:
            cnt_a +=1
        if b[s2] == answers[i]:
            cnt_b +=1
        if c[s3] == answers[i]:
            cnt_c +=1

    k = max(cnt_a, cnt_b, cnt_c)
    answer = []

    if k == cnt_a :
        answer.append(1)
    if k == cnt_b :
        answer.append(2)
    if k == cnt_c :
        answer.append(3)

    return answer

test = [1,2,3] 
for index, value in enumerate(test): 
    print(index,value)

'''
def solution(answers):
    pattern1 = [1,2,3,4,5]
    pattern2 = [2,1,2,3,2,4,2,5]
    pattern3 = [3,3,1,1,2,2,4,4,5,5]
    score = [0, 0, 0]
    result = []

    for idx, answer in enumerate(answers):
        if answer == pattern1[idx%len(pattern1)]:
            score[0] += 1
        if answer == pattern2[idx%len(pattern2)]:
            score[1] += 1
        if answer == pattern3[idx%len(pattern3)]:
            score[2] += 1

    for idx, s in enumerate(score):
        if s == max(score):
            result.append(idx+1)

    return result
'''

# 3. enumerate
# 반복문 사용 시 몇 번째 반복문인지 확인이 필요할 수 있습니다. 이때 사용합니다.
# 인덱스 번호와 컬렉션의 원소를 tuple형태로 반환합니다.
# >>> t = [1, 5, 7, 33, 39, 52]
# >>> for p in enumerate(t):
# ...     print(p)