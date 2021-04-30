'''
영어 공부에 빠져 있는 주현이는 영어 책을 자주 본다.

어느 날 영어 문장을 보면서 어떤 알파벳 문자가 많이 사용되는지 궁금해졌다.

영어 문장이 주어지면 a부터 z까지 알파벳 문자가 각각 몇 번 나왔는지 출력하는 프로그램을 작성하시오.

입력
① 90글자 이내의 영어로 된 문장이 입력된다.

② 이 문장은 영어 소문자, 공백 및 특수 문자로만 이루어져 있다.

출력
a부터 z까지 사용된 알파벳 개수를 [입출력 예시]를 참고하여 출력한다. 특수문자와 공백의 개수는 출력하지 않는다.

입력 예시   
oh! my god!

출력 예시
a:0
b:0
c:0
d:1
e:0
f:0
g:1
h:1
i:0
j:0
k:0
l:0
m:1
n:0
o:2
p:0
q:0
r:0
s:0
t:0
u:0
v:0
w:0
x:0
y:1
z:0
'''
# # 겹치면 출력
# n = str(input())

# k = [ 0 for i in range(24)]
# a = []
# c = []
# #소문자 97 ~ 123 , 대문자 65 ~ 91
# for i in range(97, 123) : 
#     ch = chr(i)
#     a.append(ch)
# print('k :', k)
# print('a :', a)

# for j in range(len(n)) :
#     z = ord(n[j])
#     c.append(z)

# print(c)

# n = str(input())
# n_pr = ''.join(char for char in n if char.isalnum())
# print(n_pr) #['o', 'h', 'm', 'y', 'g', 'o', 'd']

# a = []#a ~ z 까지 추가
# for i in range(97, 123) : 
#     ch = chr(i)
#     a.append(ch)

# for name in n_pr :
#     a[name] = a.get(name, 0) + 1
# print(a)


str = input()
li = [0 for _ in range(26)] #단어 다 채워주기
for i in str:
    if i>='a' and i<='z':
        li[ord(i)-97] +=1
    
for i in range(26):
    print("%c:%d" %(chr(i+97),li[i])) #%c :문자한개 / %d : 정수

    