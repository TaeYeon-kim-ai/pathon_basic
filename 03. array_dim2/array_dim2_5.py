'''
n이 입력되면 크기가 n인 다음과 같은 2차원 배열을 출력하시오.

입력 예)
3
출력 예)
1 2 3
8 9 4
7 6 5
입력
2차원 배열의 크기 n이 입력된다.(n<=50)

출력
크기가 n인 달팽이 배열을 출력한다.(설명참조)

입력 예시   
2

출력 예시
1 2 
4 3 
'''

n = int(input())
m = [[0]*n for i in range(n)]
cnt = 0
offset = 0
row = n #행
col = n #열

while row > 0 and col > 0:
    for i in range(offset, offset+col): #열 하나씩 늘리기 가로
        cnt += 1
        m[offset][i] = cnt

    for i in range(offset+1, offset+row): # 세로
        cnt += 1
        m[i][offset+col-1] = cnt
        
    for i in range(offset+col-2, offset-1, -1): #가로
        cnt += 1
        m[offset+row-1][i] = cnt

    for i in range(offset+row-2, offset, -1): #반대세로
        cnt += 1
        m[i][offset] = cnt

    offset += 1
    row -= 2
    col -= 2

for i in range(0, n):
    for j in range(0, n):
        print(m[i][j], end=' ')
    print()