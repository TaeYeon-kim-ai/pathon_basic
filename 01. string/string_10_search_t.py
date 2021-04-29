'''
어떤 문자열이 있을 때 문자 t의 위치를 모두 찾아 출력하시오.

입력
공백이 없는 문자열이 한 줄 입력된다.(10글자 이하)

출력
소문자 t의 위치를 공백으로 분리하여 모두 출력하시오.

입력 예시   
test

출력 예시
1 4 
'''

word = str(input())

aaa = 't'
index = -1


while True :
    index = word.find(aaa, index + 1)
    if index == -1 : 
        break
    print(index + 1, end=' ')
