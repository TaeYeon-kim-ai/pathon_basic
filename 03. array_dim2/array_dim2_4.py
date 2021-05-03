'''
하나의 정수 N을 입력받아 다음과 같이 지그재그로 출력하시오.

N이 3이라면,

1 6 7

2 5 8

3 4 9

입력
정수 n이 입력된다. ( 1 <= n <= 100)

출력
n * n 배열을 수직으로 채워서 출력한다.

입력 예시   
3

출력 예시
1 6 7 
2 5 8 
3 4 9 
'''

n = int(input())

m = [[0]*n for i in range(n)]

cnt = 0

for i in range(0, n) :
    if i % 2:
        for j in range(n-1, -1, -1):
            cnt += 1
            m[j][i] = cnt
    
    else : 
        for j in range(0, n) :
            cnt += 1
            m[j][i] = cnt

for i in range(0, n) :
    for j in range(0, n) :
        print(m[i][j], end=' ') 
    print()