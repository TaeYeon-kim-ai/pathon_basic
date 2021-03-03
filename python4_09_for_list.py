a = [1,2,3,4,5,6,7]

# for <요소변수이름> in 리스트 : 
#     코드

for element in a :
    print(element)

# list_a.extend(list_a) #한번 더 추가
# list_a.append(10) # 10 추거
# list_a.insert(3,0) # 3번째에 0 추가
# list_a.remove(3) # 3 제거
# list_a.pop(3) # 3 제거
# list_a.clear() # 모든내용 지우기


#========================

numbers = [273, 103, 5, 32, 65, 9 ,72, 800, 99]

for number in numbers : 
    if number >= 0 :
        print("100 이상의 수 : {}".format(number))

for number in numbers : 
    if number % 2 == 0 :
        print("{}는 짝수입니다".format(number))
    else : 
        print("{}는 홀수입니다".format(number))

#===========================
for number in numbers : 
    print("{}는 {}자리수입니다.".format(number, len(str(number))))


#==================================

list_of_list = [
    [1,2,3],
    [4,5,6,7],
    [8,9]
]

for a in list_of_list :
    #[1,2,3]> [4,5,6,7] > [8,9]
    for b in a :
        #1,2,3 // 4 5 6 7/ /  8 9
        print(b)

 #list가 중첩되어 있으면 for반복문도 중첩해야한다
#======================

numbers = [1,2,3,4,5,6,7,8,9]
output = [[], [], []]

for number in numbers : 
    #1,2,3,4,5,6,7,8,9
    output[(number - 1) % 3].append(number)

print(output) #

#==========================
numbers = [273, 103, 5, 32, 65, 9 ,72, 800, 99]

holzzak = ["짝수", "홀수"]
for number in numbers : 
    print("{}는 {}입니다.".format(number, holzzak[number % 2])) # 0은 첫번째자리수, 1은 두번째자리수 무조건 실수 반환
# 273는 홀수입니다.
# 103는 홀수입니다.
# 5는 홀수입니다.
# 32는 짝수입니다.
# 65는 홀수입니다.
# 9는 홀수입니다.
# 72는 짝수입니다.
# 800는 짝수입니다.
# 99는 홀수입니다.\\\

#반복문은 중첩할 수 있다.
#반복문과 조건문은 함께 사용할 수 있다.
#리스트 대괄호 내부에는 연산한 결과를 사용할 수 있고 나머지 연산자를 사용할 수도 있다.

#피라미드 만들기

for i in range(5) :
    print('*' * (i +1))

for i in range(5) :
    print('{:<5}'.format('*' * (i+1)))

# *
# **
# ***
# ****
# *****
# *
# **
# ***
# ****
# *****



