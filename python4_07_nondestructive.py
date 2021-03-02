#비파괴적 함수 : 함수를 실행하기 전과 후가 값이 유지된다
a = "hello"

print(a.upper())#HELLO
print(a)#hello

b = a.upper()
print(b) #HELLO

b = [1,2,3]
b+[4]
print(b) # [1, 2, 3]

c = b+[4]
print(c) #[1, 2, 3, 4]