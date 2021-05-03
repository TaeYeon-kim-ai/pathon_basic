'''
하나의 정수N을 입력받아 다음과 같이 작성하시오.

지그재그로 출력하시오.

N이 5라면 다음과 같이 출력한다.

1 2 3 4 5

10 9 8 7 6

11 12 13 14 15

20 19 18 17 16

21 22 23 24 25

입력
한개의 정수가 입력된다. (2<=N<=50)

출력
N*N배열을 지그재그 형태로 출력한다. (숫자와 숫자사이는 공백으로 구분한다.)

입력 예시   
3

출력 예시
1 2 3 
6 5 4 
7 8 9 
'''

n = int(input())

m = [[0]*n for i in range(n)]

cnt = 0

for i in range(0, n) : 
    if i % 2 :
        for j in range(n-1, -1, -1) : #n-1 부터 끝까지 반대로 출력
            cnt += 1
            m[i][j] = cnt
    else : 
        for j in range(0, n) :
            cnt += 1
            m[i][j] = cnt

for i in range(0, n) :
    for j in range(0, n) :
        print(m[i][j], end=' ')
    print()



    




