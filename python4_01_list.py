#반복문
#list개요
#list만들기
#list연산자

#리스트 = 목록

#순서 없는목록 #순서 있는 목록
# - 프로그래밍 = 순서있는 목록으로 구성 
#파이썬 리스트 - 0, 1, 2....

print(['수박', '바나나', '키위'])
#['수박', '바나나', '키위']

a = ['수박', '바나나', '키위', 1, 2, True]
print(a[0])
# ['수박', '바나나', '키위']
# 수박

a = [[1,2,3], [4,5,6], [7,8,9]]
print(a[0]) #[1, 2, 3]

a = ["문자열"]
print(a[0])
print(a[0][0])
print(a[0][1])
print(a[0][2])
# 문자열
# 문
# 자
# 열

a = [1,2,3,4,5]
print(a[4])
#IndexError: list index out of range


print([1,2,3] + [4,5,6])
#[1, 2, 3, 4, 5, 6]
