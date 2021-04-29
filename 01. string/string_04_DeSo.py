'''
주어지는 문장의 대문자를 소문자로, 소문자를 대문자로 변경하는 프로그램을 작성하라.

입력
한 줄의 공백없는 문장이 입력된다.(최대 길이:1000)

출력
대소문자를 서로 변환한 결과를 출력한다.

입력 예시   
CodeChallenge2014withMSP

출력 예시
cODEcHALLENGE2014WITHmsp
'''
#대소문자 변환 upper, lower, swapcase

word = str(input())
result = word.swapcase()
print(result)