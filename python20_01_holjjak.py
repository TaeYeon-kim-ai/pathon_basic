#1부터 그 수까지 짝수만 합해 출력한다.
#5넣으면 6나옴.

n = int(input())
aaa = []
for i in range(1, n + 1): # 1~ aaa+1까지 길이
    if i % 2 == 0 : #i를 2로 나누었을 때 나머지가 0이 아니면 홀수
        aaa.append(i)

print(sum(aaa))